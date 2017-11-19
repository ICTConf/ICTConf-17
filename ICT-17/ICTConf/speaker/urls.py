
from django.conf.urls import url
from django.contrib import admin

from speaker import views

app_name = "speaker"

urlpatterns = [
    url(r'^$', views.Speakers, name="speakers"),
]
