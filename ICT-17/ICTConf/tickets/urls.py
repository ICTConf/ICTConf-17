
from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = "tickets"

urlpatterns = [
    url(r'^validate_participant$', views.validate_participant, name='validat_participants'),
    url(r'^send_mail$', views.send_mail, name='send_mail'),
    url(r'^bulten', views.bulten, name='bulten'),

]