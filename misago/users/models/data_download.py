from django.db import models
from django.utils import timezone


class DataDownload(models.Model):
    STATUS_PENDING = 0
    STATUS_PROCESSING = 1
    STATUS_READY = 2
    STATUS_EXPIRED = 3

    requester_name = models.CharField(max_length=255)
    requested_on = models.DateTimeField(default=timezone.now, db_index=True)
    expires_on = models.DateTimeField(default=timezone.now)