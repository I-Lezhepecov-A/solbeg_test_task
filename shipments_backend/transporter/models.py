from django.db import models

from direction.models import Direction


class Transporter(models.Model):
    name = models.CharField(max_length=64, default=None, null=True, blank=True)
    phone = models.CharField(max_length=32, default=None, null=True,
                             blank=True)
    residence = models.ForeignKey(to=Direction, on_delete=models.CASCADE,
                                  related_name='transporters')

    def __str__(self) -> str:
        return self.name
