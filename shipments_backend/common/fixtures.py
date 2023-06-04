import pytest
from django.utils import timezone

from direction.models import Direction
from shipments.models import Shipment
from transporter.models import Transporter

from .faker import fake


@pytest.fixture(autouse=True)
def dir_factory(fake=fake):
    payload = {
        'city': fake.city(),
        'country': fake.country()
    }
    direction = Direction(**payload)
    direction.save()
    return direction


# @pytest.fixture(autouse=True)
# def direction_payload_factory(fake=fake):
#     payload = {
#         'city': fake.city(),
#         'country': fake.country()
#     }
#     return payload


@pytest.fixture(autouse=True)
def transporter_factory(fake=fake):
    payload = {
        'city': fake.city(),
        'country': fake.country()
    }
    direction = Direction(**payload)
    direction.save()
    payload = {
        "name": fake.name(),
        "phone": fake.phone_number(),
        "residence_id": direction.id
    }
    transporter = Transporter(**payload)
    transporter.save()
    return transporter


# @pytest.fixture(autouse=True)
# def transporter_payload_factory(fake=fake):
#     residence = dir_factory
#     payload = {
#         "name": fake.name(),
#         "phone": fake.phone_number(),
#         "residence_id": residence.id
#     }
#     return payload


@pytest.fixture(autouse=True)
def shipment_factory(fake=fake):
    payload = {
            'to_direction': dir_factory.id,
            'transporter': transporter_factory.id,
            'is_arrived': False,
            'sent_date': timezone.now() - timezone.timedelta(days=365),
            'estimated_arrival_date': timezone.now() - timezone.timedelta(
                days=180)
        },
    transporter = Shipment(**payload)
    transporter.save()
    return transporter


# @pytest.fixture(autouse=True)
# def shipment_payload_factory(fake=fake):
#     payload = {
#             'to_direction': dir_factory.id,
#             'transporter': transporter_factory.id,
#             'is_arrived': False,
#             'sent_date': timezone.now() - timezone.timedelta(days=365),
#             'estimated_arrival_date': timezone.now() - timezone.timedelta(
#                 days=180)
#         },
#     return payload
