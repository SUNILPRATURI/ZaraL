from django.core.exceptions import ValidationError
from django.db import models
from course.models import Course
# Create your models here.

class Assignment(models.Model):
    code = models.CharField(max_length=155,unique=True, blank=False,verbose_name='Assignment Code')
    name = models.CharField(max_length=155,null=False,blank=False,verbose_name='Assignment Name')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Assignment Description',null=False,blank=False)
    #files = models.FileField(verbose_name='Files',upload_to='media/')
    marks = models.PositiveIntegerField(verbose_name='Maximum Score',null=False,blank=False)
    status = models.BooleanField(verbose_name="Status",default=True)
    
    
    def __str(self):
        return self.code
    
    
class Submission(models.Model):
    code = models.CharField(max_length=155,primary_key=True,verbose_name='Assignment Code')
    name = models.CharField(max_length=155,null=False,blank=False,verbose_name='Assignment Name')
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Assignment Description',null=False,blank=False)
    #files = models.FileField(verbose_name='Files',upload_to='media/',null=True)
    score = models.PositiveIntegerField(default=0,verbose_name='Student Score')
    
    
    
    
    def __str(self):
        return self.code
    
    def clean(self):
        super().clean()
        if self.score > self.assignment.marks:
            raise ValidationError("Score cannot be higher than maximum marks")

    def save(self, *args, **kwargs):
        self.clean()  
        
        super().save(*args, **kwargs) 
 