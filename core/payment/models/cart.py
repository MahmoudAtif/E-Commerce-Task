from typing import Any
from django.db import models
from django.db.models.aggregates import Sum
from django.db.models.functions import Coalesce
from core.utils.utils_models import AbstractModel
from django.utils.translation import gettext_lazy as _


class Cart(AbstractModel):
    user = models.OneToOneField(
        'core.User',
        verbose_name=_('User'),
        on_delete=models.CASCADE
    )
    total = models.DecimalField(
        verbose_name=_('Total'),
        max_digits=8,
        decimal_places=2,
        default=0
    )

    class Meta:
        db_table = 'payment_cart'
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        # When the instance is calling --> recalculate cart
        if self.id:
            self._recalculate_cart()

    def __str__(self):
        return str(self.user)

    def _calculate_total(self):
        """Calculate total price for all products in a cart"""

        total = self.items.aggregate(
            sum=Coalesce(
                Sum(models.F('product__price') * models.F('quantity')),
                0,
                output_field=models.DecimalField(
                    max_digits=8,
                    decimal_places=2
                )
            )
        )['sum']
        self.total = total
        return self.total

    def _recalculate_cart(self):
        self._calculate_total()
        self.save()

    def clear(self):
        """Clear Cart"""
        self.total = 0
        self.items.all().delete()
        self.save()
        return True

    def add_item(self, product, quantity: int):
        item = self.items.create(
            product=product,
            quantity=quantity
        )
        return item

    @property
    def get_total_items(self):
        total = self.items.aggregate(
            sum=Coalesce(
                Sum(models.F('quantity')),
                0,
                output_field=models.IntegerField()
            ),
        )['sum']
        return total
