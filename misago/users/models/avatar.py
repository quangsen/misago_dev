from django.db import models
from ..avatars import store


class Avatar(models.Model):
    size = models.PositiveIntegerField(default=0)
    image = models.ImageField(max_length=255, upload_to=store.upload_to)
