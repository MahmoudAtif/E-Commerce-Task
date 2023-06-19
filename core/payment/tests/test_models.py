from rest_framework.test import APITestCase
from core.users.models import User
from core.payment.models import Cart, Order
from core.products.models import Product
from decimal import Decimal


class TestModel(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='newUser2',
            email='newUser2@gmail.com',
            password='newUser2'
        )
        self.cart, created = Cart.objects.get_or_create(user=self.user)
        self.product = Product.objects.create(name='product2', price=80)
        self.order = Order.objects.create(
            user=self.user,
            total=self.cart.total,
            state='cairo',
            city='naser city'
        )

    def test_cart_values(self):
        """Test cart values"""
        self.assertEqual(self.cart.total, Decimal('0'))
        self.assertEqual(self.cart.user, self.user)

    def test_cart_add_item(self):
        """Test add item to cart"""
        item = self.cart.add_item(self.product, quantity=2)
        self.assertEqual(item.cart, self.cart)
        self.assertEqual(item.product, self.product)
        self.assertEqual(item.quantity, 2)

    def test_order_values(self):
        """Test order values"""
        self.assertEqual(self.order.total, self.cart.total)
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.state, 'cairo')
        self.assertEqual(self.order.city, 'naser city')
        self.assertEqual(self.order.status, Order.StatusEnum.INITIATED)

    def test_add_order_item(self):
        """Test add item to order"""
        item = self.order.items.create(
            product=self.product,
            quantity=3,
            price=self.product.price
        )
        self.assertEqual(item.order, self.order)
        self.assertEqual(item.product, self.product)
        self.assertEqual(item.quantity, 3)
        self.assertEqual(item.price, self.product.price)
