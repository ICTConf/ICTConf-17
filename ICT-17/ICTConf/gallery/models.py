from django.db import models
import os

# Create your models here.

def upload_file(instance, filename):
    return os.path.join('gallery/%s/' % instance.name, filename)

class Gallery(models.Model):
    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to=upload_file)


    def __str__(self):
        return self.name
