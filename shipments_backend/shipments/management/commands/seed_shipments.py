from typing import Any

from django.core.management.base import BaseCommand
from django.utils import timezone

from direction.models import Direction
from shipments.models import Shipment
from transporter.models import Transporter


class Command(BaseCommand):
    shipments = [
        {
            'to_direction': Direction.objects.filter(country='Belarus',
                                                     city='Minsk').first(),
            'transporter': Transporter.objects.last(),
            'is_arrived': True,
            'sent_date': timezone.now() - timezone.timedelta(days=365),
            'estimated_arrival_date': timezone.now()
        },
        {
            'to_direction': Direction.objects.filter(country='Lithuania',
                                                     city='Vilnus').first(),
            'transporter': Transporter.objects.first(),
            'is_arrived': True,
            'sent_date': timezone.now() - timezone.timedelta(days=365),
            'estimated_arrival_date': timezone.now() + timezone.timedelta(
                days=10)
        },
        {
            'to_direction': Direction.objects.filter(country='Poland',
                                                     city='Warsaw').first(),
            'transporter': Transporter.objects.get(pk=5),
            'is_arrived': False,
            'sent_date': timezone.now() - timezone.timedelta(days=180),
            'estimated_arrival_date': timezone.now() + timezone.timedelta(
                days=180)
        },
        {
            'to_direction': Direction.objects.filter(country='Germany',
                                                     city='Dresden').first(),
            'transporter': Transporter.objects.get(pk=2),
            'is_arrived': False,
            'sent_date': timezone.now() - timezone.timedelta(days=365),
            'estimated_arrival_date': timezone.now() - timezone.timedelta(
                days=180)
        },
        {
            'to_direction': Direction.objects.filter(country='Austria',
                                                     city='Viena').first(),
            'transporter': Transporter.objects.get(pk=7),
            'is_arrived': False,
            'sent_date': timezone.now(),
            'estimated_arrival_date': timezone.now() + timezone.timedelta(
                days=180)
        },
    ]

    def handle(self, *args: Any, **options: Any) -> None:
        rows = [Shipment(**shipment) for shipment in self.shipments]
        Shipment.objects.bulk_create(rows)
