from django.shortcuts import render
from django.http import HttpResponse
from .forms import FileUploadForms
from django.template.context_processors import csrf
from django.template import RequestContext

# Create your views here.
def file_upload(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST' :
        form = FileUploadForms(request.POST, request.FILES)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            #sender_email = form.cleaned_data['email']
            #description = form.cleaned_data['description']
            form.save()
            return HttpResponse("Thanks " + sender_name + " for submitting your form")
    else:
        form = FileUploadForms()
    return render(request, 'file_upload.html', {'form': form})

