from django.db import models
import os
class SponsorShipLevel(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name



def upload_file(instance, filename):
    return os.path.join('sponsorship/%s/' % instance.sponsorship_name, filename)

class SponsorShip(models.Model):

    level_id = models.ForeignKey(SponsorShipLevel,default=0)
    sponsorship_name = models.CharField(max_length=255)
    sponsorship_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=upload_file)

    def __str__(self):
        return self.sponsorship_name


