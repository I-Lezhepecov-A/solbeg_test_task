from django.db import models


class Direction(models.Model):
    country = models.CharField(max_length=128, default=None, null=True,
                               blank=True)
    city = models.CharField(max_length=128, default=None, null=True,
                            blank=True)

    def __str__(self) -> str:
        return f'{self.country}, {self.city}'
