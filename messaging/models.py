
from django.db import models

from django.utils import timezone

class Message(models.Model):
        sender = models.CharField(max_length=100)
        receiver = models.CharField(max_length=100)
        content = models.TextField(blank=False,null=False)
        date = models.DateField(default=timezone.now)



