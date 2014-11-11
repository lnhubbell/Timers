from django.db import models


class Timer(models.Model):
    name = models.CharField(max_length=255)
    seconds = models.PositiveIntegerField(default=0,
                                          verbose_name="Time in Seconds")
