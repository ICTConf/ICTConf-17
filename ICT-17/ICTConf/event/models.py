# -*- coding: UTF-8 -*-

import os
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

def upload_file(instance, filename):

    return os.path.join('event/%s/' % instance.title, filename)

class Event(models.Model):

    speaker = models.ForeignKey("speaker.Speaker",
                                related_name="events")
    photo = models.ImageField(upload_to=upload_file)
    title = models.CharField(max_length=140)
    content = models.TextField(max_length=300)
    hall = models.CharField(default="Konferans Salonu",
                            max_length=40)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        unique_together = ["title", "speaker"]
        ordering = ["start_date"]

    def __str__(self):
        return self.title

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError(message="Konuşmanın Başlangıç Zamanı Bitişten Önce Olmalı")
