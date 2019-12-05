from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator


class Currency(models.Model):
    # base currency is BGN
    full_name = models.CharField(max_length=200, unique=True)
    currency_abbr = models.CharField(max_length=200, unique=True)
    rate_vs_base = models.DecimalField(max_digits=20, decimal_places=6, validators=[MinValueValidator(Decimal('0.000001'))])

    class Meta:
        ordering = ('currency_abbr',)

    def convert_to(self, currency, amount=Decimal(1)):
        return Decimal(amount) * (self.rate_vs_base / currency.rate_vs_base)

    def __str__(self):
        return '{} : {}'.format(self.currency_abbr, self.rate_vs_base)
