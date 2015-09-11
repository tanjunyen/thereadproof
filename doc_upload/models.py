from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField()
    description = models.CharField(max_length=1000)
    file = models.FileField(upload_to='files_to_proofread')