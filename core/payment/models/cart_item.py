from django.db import models
from core.utils.utils_models import AbstractModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


class CartItem(AbstractModel):
    cart = models.ForeignKey(
        'core.Cart',
        verbose_name=_('Cart'),
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        'core.Product',
        verbose_name=_('Product'),
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_('Quantity'),
        validators=[
            MinValueValidator(1)
        ],
        default=1
    )

    class Meta:
        db_table = 'payment_cart_item'
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')

    def __str__(self) -> str:
        return f'{self.cart} | {self.product}'

    def update_quantity(self, quantity: int):
        self.quantity = quantity
        self.save()
        return True
