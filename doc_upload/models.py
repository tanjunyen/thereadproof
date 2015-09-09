from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.CharField(max_length=1000)