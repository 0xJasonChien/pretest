from typing import Self

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from pretest.config import settings

from .models import Product


# Create your tests here.
class OrderTestCase(APITestCase):

    def setUp(self: Self) -> None:
        self.valid_token = settings.ACCEPTED_TOKEN[0]
        self.invalid_token = 'invalid-token'  # noqa: S105

        self.product_data = {
            'name': 'Test Product',
            'price': 100.0,
            'quantity': 10,
        }
        self.order_data = {
            'products': [
                {'product': {'uuid': None}, 'quantity': 2},
            ],
        }

    def test_import_product_success(self: Self) -> None:
        url = reverse('import_product')
        data = {**self.product_data, 'token': self.valid_token}

        response = self.client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Product.objects.count() == 1
        assert response.data['name'] == 'Test Product'

    def test_import_product_invalid_token(self: Self) -> None:
        url = reverse('import_product')
        data = {**self.product_data, 'token': self.invalid_token}

        response = self.client.post(url, data, format='json')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Product.objects.count() == 0
