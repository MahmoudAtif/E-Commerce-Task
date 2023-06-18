from django.db import models
from core.utils.utils_models import AbstractModel
from django.utils.translation import gettext_lazy as _


class OrderItem(AbstractModel):
    order = models.ForeignKey(
        'core.Order',
        verbose_name=_('Order'),
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "core.Product",
        verbose_name=_('Product'),
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(verbose_name=_('Quantity'),)
    price = models.DecimalField(
        verbose_name=_('Price'),
        max_digits=8,
        decimal_places=2
    )

    class Meta:
        db_table = 'payment_order_item'
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')

    def __str__(self):
        return f'{self.cart} | {self.product}'
