import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from common.fixtures import dir_factory, fake


@pytest.mark.django_db
def test_get_transporters_should_return_200():
    client = APIClient()
    response = client.get(reverse('transpoters-list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_transporter_should_return_201(dir_factory):  # noqa
    client = APIClient()

    payload = {
        "name": fake.name(),
        "phone": fake.phone_number(),
        "residence_id": dir_factory.id
    }
    response = client.post(reverse('transpoters-list'), payload, 'json')
    assert response.status_code == 201

    payload = {
        "name": fake.name(),
        "phone": fake.phone_number(),
        "residence_id": dir_factory.id + 123
    }
    response = client.post(reverse('transpoters-list'), payload, 'json')
    assert response.status_code == 400
