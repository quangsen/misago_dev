from django.db import models


class ActivityRanking(models.Model):
    score = models.PositiveIntegerField(default=0, db_index=True)