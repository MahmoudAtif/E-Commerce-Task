from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from core.products import views


class TestUrl(APITestCase):

    def test_products_list_view(self):
        url = reverse('products:products-list')
        view = resolve(url).func.cls
        self.assertEqual(view, views.ProductViewSet)

    def test_product_retrieve_view(self):
        url = reverse('products:products-detail', args=[1])
        view = resolve(url).func.cls
        self.assertEqual(view, views.ProductViewSet)
