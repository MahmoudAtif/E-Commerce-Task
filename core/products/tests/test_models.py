from rest_framework.test import APITestCase
from core.products.models import Product


class TestModel(APITestCase):

    def test_create_product(self):
        product = Product.objects.create(
            name='testPro',
            price=100
        )
        self.assertEqual(product.name, 'testPro')
        self.assertEqual(product.price, 100)
