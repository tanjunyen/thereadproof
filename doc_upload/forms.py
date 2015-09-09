from django.forms import ModelForm
from .models import Job

class FileUploadForms(ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'email', 'description', 'file']