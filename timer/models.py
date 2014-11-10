from django.db import models


class Timer(models.Model):
    owner = models.ForeignKey('auth.User', related_name='timers')
    name = models.CharField(max_length=255)
    seconds = models.PositiveIntegerField(default=0,
                                          verbose_name="Time in Seconds")

    def increment_time(self, seconds):
        self.seconds += seconds
