from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from core.products.models import Product


class TestView(APITestCase):

    def setUp(self) -> None:
        self.product = Product.objects.create(
            name='NewPro',
            price=50
        )

    def test_products_list_view(self):
        """Test Products List View"""
        url = reverse('products:products-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_retrieve_view(self):
        """Test Product Retrieve View"""
        url = reverse(
            'products:products-detail',
            kwargs={'pk': self.product.pk}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_product_pk_retrieve_view(self):
        """Test Product Retrieve with wrong pk"""
        url = reverse(
            'products:products-detail',
            kwargs={'pk': 55}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_search_view(self):
        url = reverse('products:products-list') + "?search=T"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
