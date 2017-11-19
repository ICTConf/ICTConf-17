# -*- coding: UTF-8 -*-

import os

from django.db import models


# Create your models here.


def upload_file(instance, filename):

    return os.path.join('speaker/%s/' % instance.name, filename)

class Speaker(models.Model):

    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to=upload_file)
    company = models.CharField(max_length=140)
    github = models.CharField(max_length=140, blank=True)
    linkedin = models.CharField(max_length=140, blank=True)
    twitter = models.CharField(max_length=140, blank=True)
    mission = models.CharField(max_length=40)
    slug = models.SlugField(unique=True,
                            max_length=80,
                            editable=False)



    def __str__(self):
        return self.slug
