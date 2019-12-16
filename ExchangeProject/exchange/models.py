from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator


class Currency(models.Model):
    full_name = models.CharField(max_length=200, unique=True)
    currency_abbr = models.CharField(max_length=200, unique=True)
    rate_vs_base = models.DecimalField(max_digits=20,
                                       decimal_places=9,
                                       validators=[MinValueValidator(Decimal('0.000001'))])

    class Meta:
        ordering = ('currency_abbr',)
        verbose_name_plural = 'currencies'

    def convert_to(self, currency, amount=Decimal(1)):
        return Decimal(amount) * (Decimal(self.rate_vs_base) / Decimal(currency.rate_vs_base))

    def __str__(self):
        return '{} : {}'.format(self.currency_abbr, self.rate_vs_base)
