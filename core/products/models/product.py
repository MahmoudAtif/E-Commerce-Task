from django.db import models
from django.utils.translation import gettext_lazy as _
from core.utils.utils_models import AbstractModel


class Product(AbstractModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    price = models.DecimalField(
        verbose_name=_('Price'),
        max_digits=8,
        decimal_places=2
    )
    status = models.BooleanField(verbose_name=_('Status'), default=True)
    
    class Meta:
        db_table = 'products_product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self) -> str:
        return self.name
