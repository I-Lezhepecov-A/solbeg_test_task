import pytest
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient

from common.fixtures import dir_factory, fake, transporter_factory  # noqa
from direction.models import Direction

from .models import Shipment


@pytest.mark.django_db
def test_get_shipments_should_return_200():
    client = APIClient()
    response = client.get(reverse('shipments-list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_shipment_should_return_201(dir_factory, transporter_factory):  # noqa
    client = APIClient()
    direction = dir_factory
    payload = {
        "estimated_arrival_date": timezone.now() + timezone.timedelta(days=365),
        "sent_date": timezone.now(),
        "to_direction": {
            "country": direction.country,
            "city": direction.city
        },
        "transporter_id": transporter_factory.id
    }
    response = client.post(reverse('shipments-list'), payload, 'json')
    assert response.status_code == 201

    direction = dir_factory
    payload = {
        "estimated_arrival_date": timezone.now(),
        "sent_date": timezone.now() + timezone.timedelta(days=365),
        "to_direction": {
            "country": direction.country,
            "city": direction.city
        },
        "transporter_id": transporter_factory.id + 123
    }
    response = client.post(reverse('shipments-list'), payload, 'json')
    assert response.status_code == 400

    direction = dir_factory
    payload = {
        "estimated_arrival_date": timezone.now() + timezone.timedelta(days=365),  # noqa
        "sent_date": timezone.now(),
        "to_direction": {
            "country": direction.country,
            "city": direction.city + "fake_city"
        },
        "transporter_id": transporter_factory.id + 123
    }
    response = client.post(reverse('shipments-list'), payload, 'json')
    assert response.status_code == 400

    direction = dir_factory
    payload = {
        "estimated_arrival_date": timezone.now() + timezone.timedelta(days=365),  # noqa
        "sent_date": timezone.now(),
        "to_direction": {
            "country": direction.country,
            "city": direction.city + "fake_city"
        },
        "transporter_id": transporter_factory.id
    }
    response = client.post(reverse('shipments-list'), payload, 'json')
    assert response.status_code == 201
    assert Direction.objects.get(country=direction.country,
                                 city=direction.city + "fake_city")


@pytest.mark.django_db
def test_get_shipment_detail_should_return_200(dir_factory, transporter_factory):  # noqa
    client = APIClient()
    direction = dir_factory
    payload = {
        "estimated_arrival_date": timezone.now() + timezone.timedelta(days=365),  # noqa
        "sent_date": timezone.now(),
        "to_direction": {
            "country": direction.country,
            "city": direction.city
        },
        "transporter_id": transporter_factory.id
    }
    response = client.post(reverse('shipments-list'), payload, 'json')
    assert response.status_code == 201

    response = client.get(reverse('shipments-detail',
                                  args=[response.json()['id']]))
    assert response.status_code == 200

    response = client.get(reverse('shipments-detail',
                                  args=[response.json()['id'] + 1]))
    assert response.status_code == 404


@pytest.mark.django_db
def test_destroy_shipment_detail_should_return_204(dir_factory, transporter_factory):  # noqa
    client = APIClient()
    direction = dir_factory
    payload = {
        "estimated_arrival_date": timezone.now() + timezone.timedelta(days=365),  # noqa
        "sent_date": timezone.now(),
        "to_direction": {
            "country": direction.country,
            "city": direction.city
        },
        "transporter_id": transporter_factory.id
    }
    response = client.post(reverse('shipments-list'), payload, 'json')
    id = response.json()['id']
    assert response.status_code == 201

    response = client.get(reverse('shipments-detail',
                                  args=[id]))
    assert response.status_code == 200

    response = client.delete(reverse('shipments-detail',
                                     args=[id]))
    assert response.status_code == 204

    response = client.get(reverse('shipments-detail',
                                  args=[id]))
    assert response.status_code == 404

    assert Shipment.objects.get(pk=id).is_deleted


@pytest.mark.django_db
def test_partitial_update_shipment_detail_should_return_204(dir_factory, transporter_factory):  # noqa
    client = APIClient()
    direction = dir_factory
    payload = {
        "estimated_arrival_date": timezone.now() + timezone.timedelta(days=365),  # noqa
        "sent_date": timezone.now(),
        "to_direction": {
            "country": direction.country,
            "city": direction.city
        },
        "transporter_id": transporter_factory.id
    }
    response = client.post(reverse('shipments-list'), payload, 'json')
    id = response.json()['id']
    assert response.status_code == 201

    payload = {
        "is_arrived": True
    }

    response = client.patch(reverse('shipments-detail',
                                    args=[id]), payload)
    assert response.status_code == 200

    assert Shipment.objects.get(pk=id).is_arrived
