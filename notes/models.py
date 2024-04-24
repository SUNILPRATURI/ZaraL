from django.db import models
from course.models import Course
# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=155,null=False,blank=False,verbose_name='Notes Topic')
    Course = models.ForeignKey(Course,on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Notes ',null=False,blank=False)
    
    
    
    def __str(self):
        return self.code