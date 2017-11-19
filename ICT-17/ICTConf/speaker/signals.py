q# -*- coding: UTF-8 -*-

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from speaker.models import Speaker


@receiver(post_save, sender=Speaker)
def update_slug(sender, **kwargs):

    if kwargs["instance"].name + " " +kwargs["instance"].last_name != kwargs["instance"].slug \
            or kwargs["instance"].slug is None:
        slug = slugify(kwargs['instance'].name.replace('i', 'i') + " " +
                       kwargs["instance"].last_name.replace("i","i"))
        Speaker.objects.filter(id=kwargs['instance'].id).update(slug=slug)
