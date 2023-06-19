from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from core.payment import views


class TestUrl(APITestCase):

    def test_cart_list_url(self):
        """Test cart list url"""
        url = reverse('payment:cart-list')
        view = resolve(url).func.cls
        self.assertEqual(view, views.CartView)

    def test_add_to_cart_url(self):
        """Test Add to cart url"""
        url = reverse('payment:cart-add')
        view = resolve(url).func.cls
        self.assertEqual(view, views.CartView)

    def test_remove_from_cart_url(self):
        """Test remove from cart url"""
        url = reverse('payment:cart-remove', args=[1])
        view = resolve(url).func.cls
        self.assertEqual(view, views.CartView)

    def test_update_cartitem_quantity_url(self):
        """Test update cart item quantity url"""
        url = reverse('payment:cart-update-quantity', args=[1])
        view = resolve(url).func.cls
        self.assertEqual(view, views.CartView)

    def test_clear_cart_url(self):
        """Test clear cart url"""
        url = reverse('payment:cart-clear')
        view = resolve(url).func.cls
        self.assertEqual(view, views.CartView)

    def test_checkout_url(self):
        """Test checkout cart url"""
        url = reverse('payment:cart-checkout')
        view = resolve(url).func.cls
        self.assertEqual(view, views.CartView)
