from django.conf.urls import url
from django.contrib import admin

from home import views

app_name = "home"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'contact/$', views.contact, name="contact"),
    url(r'about/$', views.about, name="about"),
    url(r'schedule/$', views.schedule, name="schedule"),

    url(r'get_ticket/$', views.get_ticket, name="get_ticket"),
]
