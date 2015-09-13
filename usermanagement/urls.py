__author__ = 'tanjunyen'

from django.conf.urls import include, url
from usermanagement.views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'accounts/login/$', log_in, name="user_account_login"),
    url(r'accounts/auth/$', auth_view, name="user_account_auth"),
    url(r'accounts/logout/$', log_out, name="user_account_logout"),
    url(r'accounts/loggedin/$', logged_in, name="user_account_loggedin"),
    url(r'accounts/invalid/$', invalid_login, name="user_account_invalid"),
    url(r'accounts/registration/$', registration, name="user_account_registration"),
    url(r'accounts/register_success/$', register_success),
    url(r'doc_upload/$', doc_upload, name="user_doc_upload"),
]

