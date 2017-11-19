from django.contrib import admin

# Register your models here.
from event.models import Event

admin.site.register(Event)