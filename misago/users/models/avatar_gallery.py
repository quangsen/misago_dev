from django.db import models


class AvatarGallery(models.Model):
    gallery = models.CharField(max_length=255)