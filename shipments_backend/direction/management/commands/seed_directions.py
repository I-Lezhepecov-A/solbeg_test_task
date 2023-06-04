from typing import Any

from django.core.management.base import BaseCommand

from direction.models import Direction


class Command(BaseCommand):
    directions = [
        {
            'country': 'Belarus',
            'city': 'Minsk'
        },
        {
            'country': 'Lithuania',
            'city': 'Vilnus'
        },
        {
            'country': 'Austria',
            'city': 'Viena'
        },
        {
            'country': 'Germany',
            'city': 'Dresden'
        },
        {
            'country': 'Poland',
            'city': 'Warsaw'
        },
        {
            'country': 'Italy',
            'city': 'Rome'
        },
        {
            'country': 'China',
            'city': 'Beijing'
        },
        {
            'country': 'Belarus',
            'city': 'Borisov'
        },
        {
            'country': 'Latvia',
            'city': 'Riga'
        },
        {
            'country': 'Hunagry',
            'city': 'Budapesht'
        },
    ]

    def handle(self, *args: Any, **options: Any) -> None:
        rows = [Direction(**direction) for direction in self.directions]
        Direction.objects.bulk_create(rows)
        # return super().handle(*args, **options)
