from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from core.users.models import User
from core.payment.models import Cart
from core.products.models import Product
from core.utils.response_codes import GeneralCodes


class TestView(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='newUser',
            email='newUser@gmail.com',
            password='newUser'
        )
        self.product = Product.objects.create(name='product1', price=80)
        self.cart, created = Cart.objects.get_or_create(user=self.user)
        self.cart_item = self.cart.items.create(
            product=self.product,
            quantity=2
        )
        self.client.force_authenticate(self.user)

    def test_cart_list_view(self):
        """Test cart list for authenticated user"""
        url = reverse('payment:cart-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('code'), GeneralCodes.SUCCESS)

    def test_add_to_cart_view(self):
        """Test add to cart view"""
        url = reverse('payment:cart-add')
        data = {
            "product": self.product.id,
            "quantity": 1
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('code'), GeneralCodes.SUCCESS)

    def test_remove_from_cart_view(self):
        """Test remove from cart view"""
        url = reverse('payment:cart-remove', kwargs={'pk': self.cart_item.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('code'), GeneralCodes.SUCCESS)

    def test_update_quantity_view(self):
        """Test update quantity view"""
        url = reverse(
            'payment:cart-update-quantity',
            kwargs={'pk': self.cart_item.id}
        )
        data = {
            "quantity": 6
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('code'), GeneralCodes.SUCCESS)

    def test_checkout_view(self):
        """Test checkout view"""
        url = reverse('payment:cart-checkout')
        data = {
            "state": "cairo",
            "city": "Naser city"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('code'), GeneralCodes.SUCCESS)

    def test_clear_cart_view(self):
        """Test clear cart view"""
        url = reverse('payment:cart-clear')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('code'), GeneralCodes.SUCCESS)
