from django.db import models


class Rank(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    css_class = models.CharField(max_length=255, null=True, blank=True)
    is_default = models.BooleanField(default=False)
    is_tab = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name
