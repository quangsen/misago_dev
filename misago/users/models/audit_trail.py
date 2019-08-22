from django.db import models
from django.utils import timezone


class AuditTrail(models.Model):
    object_id = models.PositiveIntegerField()
    created_on = models.DateTimeField(db_index=True, default=timezone.now)