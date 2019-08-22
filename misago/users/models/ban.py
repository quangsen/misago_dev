from django.db import IntegrityError, models


class Ban(models.Model):
    USERNAME = 0
    EMAIL = 1
    IP = 2

    registration_only = models.BooleanField(default=False, db_index=True)
    banned_value = models.CharField(max_length=255, db_index=True)
    user_message = models.TextField(null=True, blank=True)
    staff_message = models.TextField(null=True, blank=True)
    expires_on = models.DateTimeField(null=True, blank=True, db_index=True)
    is_checked = models.BooleanField(default=True, db_index=True)


class BanCache(models.Model):
    cache_version = models.CharField(max_length=8)
    user_message = models.TextField(null=True, blank=True)
    staff_message = models.TextField(null=True, blank=True)
    expires_on = models.DateTimeField(null=True, blank=True)