from django.db import models
from core.utils.utils_models import AbstractModel
from django.utils.translation import gettext_lazy as _


class Order(AbstractModel):
    class StatusEnum(models.IntegerChoices):
        INITIATED = 1, "Initiated"
        CONFIRMED = 2, _('Confirmed')
        DELIVERED = 3, _('Delivered')
        CANCELED = 4, _('Canceled')

    user = models.ForeignKey(
        'core.User',
        verbose_name=_('User'),
        related_name='orders',
        on_delete=models.CASCADE
    )
    total = models.DecimalField(
        verbose_name=_('Total'),
        max_digits=8,
        decimal_places=2
    )
    state = models.CharField(verbose_name=_('State'), max_length=50)
    city = models.CharField(verbose_name=_('City'), max_length=50)
    status = models.IntegerField(
        verbose_name=_('Status'),
        choices=StatusEnum.choices,
        default=StatusEnum.INITIATED
    )

    class Meta:
        db_table = 'payment_order'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.user)
