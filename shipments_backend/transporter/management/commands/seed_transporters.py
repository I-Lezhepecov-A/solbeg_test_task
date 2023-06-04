from typing import Any

from django.core.management.base import BaseCommand

from direction.models import Direction
from transporter.models import Transporter


class Command(BaseCommand):
    transporters = [
        {
            'name': 'Belarus, Minsk LKW',
            'phone': '+375 00 123 123 32',
            'residence': Direction.objects.filter(country='Belarus',
                                                  city='Minsk').first()
        },
        {
            'name': 'Lithuania, Vilnus',
            'phone': '+375 00 123 123 32',
            'residence': Direction.objects.filter(country='Lithuania',
                                                  city='Vilnus').first()
        },
        {
            'name': 'Belarus, Minsk LKW GmbH',
            'phone': '+375 00 123 123 32',
            'residence': Direction.objects.filter(country='Belarus',
                                                  city='Minsk').first()
        },
        {
            'name': 'Austria, Viena LKW',
            'phone': '+375 00 123 123 32',
            'residence': Direction.objects.filter(country='Austria',
                                                  city='Viena').first()
        },
        {
            'name': 'Germany, Dresden LKW',
            'phone': '+375 00 123 123 32',
            'residence': Direction.objects.filter(country='Germany',
                                                  city='Dresden').first()
        },
        {
            'name': 'Poland, Warsaw LKW',
            'phone': '+375 00 123 123 32',
            'residence': Direction.objects.filter(country='Poland',
                                                  city='Warsaw').first()
        },
        {
            'name': 'Italy, Rome LKW',
            'phone': '+375 00 123 123 32',
            'residence': Direction.objects.filter(country='Italy',
                                                  city='Rome').first()
        },
        {
            'name': 'China, Beijing LKW',
            'phone': '+375 00 123 123 32',
            'residence': Direction.objects.filter(country='China',
                                                  city='Beijing').first()
        },
    ]

    def handle(self, *args: Any, **options: Any) -> None:
        rows = [Transporter(**transporter) for transporter in
                self.transporters]
        Transporter.objects.bulk_create(rows)
