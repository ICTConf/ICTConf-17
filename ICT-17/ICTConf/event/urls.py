
from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = "event"

urlpatterns = [
    url(r'^$', views.events_to_json, name="event_detail"),

]
