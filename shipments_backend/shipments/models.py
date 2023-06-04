import secrets
import string

from django.db import models

from direction.models import Direction
from transporter.models import Transporter


def code_gen():
    digits_count = 3
    letters_count = 3
    digits = string.digits
    letters = string.ascii_uppercase
    code_digits = ''.join(secrets.choice(digits) for i in range(digits_count))
    code_letters = ''.join(secrets.choice(letters) for i
                           in range(letters_count))
    return code_letters+code_digits


class Shipment(models.Model):
    code = models.CharField(default=code_gen, max_length=32)
    estimated_arrival_date = models.DateField()
    overdue = models.BooleanField(default=False)
    sent_date = models.DateField()
    is_arrived = models.BooleanField(default=False)
    to_direction = models.ForeignKey(to=Direction, on_delete=models.CASCADE,
                                     related_name='shipments')
    transporter = models.ForeignKey(to=Transporter, on_delete=models.CASCADE,
                                    related_name='shipments')
    is_deleted = models.BooleanField(default=False)
