from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from doc_upload.forms import FileUploadForms
from doc_upload.models import Job
# Create your views here.

def index(request):
    t = get_template('base.html')
    html = t.render(Context({'name': 'JunYen'}))
    return HttpResponse(html)

def log_in(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/user/accounts/loggedin')
    else:
        return HttpResponseRedirect('/user/accounts/invalid')

def logged_in(request):
    return render_to_response('loggedin.html', { 'full_name' : request.user.username })

def invalid_login(request):
    return render_to_response('invalid.html')

def log_out(request):
    logout(request)
    return render_to_response('logout.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/accounts/register_success')
    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')

def doc_upload(request):
    c = {}
    c.update(csrf(request))
    current_user = request.user

    if request.method == 'POST' :

        form = FileUploadForms(request.POST, request.FILES)

        if form.is_valid():
            job = Job(
                user = current_user,
                email = form.cleaned_data['email'],
                description = form.cleaned_data['description'],
                file = form.cleaned_data['file'],
            )
            job.save()

            return HttpResponse("Thanks " + current_user.username + " for submitting your form")
    else:
        form = FileUploadForms()
    return render(request, 'doc_upload.html', {'form': form, 'full_name' : current_user.username })
