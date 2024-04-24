from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('password', make_password(password))  # Hash the password
        user = self.model(username=username, email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    gender = models.CharField(max_length=55, choices=(("Male", "Male"), ("Female", "Female"), ("Other", "Other")))
    role = models.CharField(max_length=50, choices=(
        ("ADMIN", "Admin"),
        ("STUDENT", "Student"),
        ("INSTRUCTOR", "Instructor")
    ), default="ADMIN")

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class StudentManager(CustomUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="STUDENT")

class TeacherManager(CustomUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="INSTRUCTOR")

class Student(CustomUser):
    base_role = CustomUser.role = "STUDENT"
    objects = StudentManager()

    class Meta:
        proxy = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Instructor(CustomUser):
    base_role = CustomUser.role = "INSTRUCTOR"
    objects = TeacherManager()

    class Meta:
        proxy = True
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'
