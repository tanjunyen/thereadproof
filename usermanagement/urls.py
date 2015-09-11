__author__ = 'tanjunyen'

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'accounts/login/$', views.log_in),
    url(r'accounts/auth/$', views.auth_view),
    url(r'accounts/logout/$', views.log_out),
    url(r'accounts/loggedin/$', views.logged_in),
    url(r'accounts/invalid/$', views.invalid_login),
    url(r'accounts/registration/$', views.registration),
    url(r'accounts/register_success/$', views.register_success),

    url(r'doc_upload/$', views.doc_upload),
]

