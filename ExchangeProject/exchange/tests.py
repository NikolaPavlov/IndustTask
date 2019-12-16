from decimal import Decimal

from django.test import TestCase

from .models import Currency


class CurrencyTestCase(TestCase):

    def setUp(self):
        self.bgn = Currency(full_name='Bulgarian Lev',
                            currency_abbr='BGN',
                            rate_vs_base=Decimal('1').quantize(Decimal('1.000000')))

        self.usd = Currency(full_name='United States Dollar',
                            currency_abbr='USD',
                            rate_vs_base=Decimal('1.76296').quantize(Decimal('1.000000')))

        self.aud = Currency(full_name='Australian Dollar',
                            currency_abbr='AUD',
                            rate_vs_base=Decimal('1.20805').quantize(Decimal('1.000000')))

    def test_convert_1USD_to_BGN(self):
        result = self.usd.convert_to(self.bgn)
        self.assertEqual(result, Decimal('1.76296'))

    def test_convert_5USD_to_BGN(self):
        result = self.usd.convert_to(self.bgn, Decimal(5))
        self.assertEqual(result, Decimal('8.81480'))

    def test_convert_1BGN_to_USD(self):
        result = self.bgn.convert_to(self.usd, '1')
        self.assertEqual(result, Decimal('0.5672278440804102191768389527'))

    def test_convert_5BGN_to_USD(self):
        result = self.bgn.convert_to(self.usd, Decimal(5))
        self.assertEqual(result, Decimal('2.836139220402051095884194764'))

    def test_convert_1USD_to_AUD(self):
        result = self.usd.convert_to(self.aud)
        self.assertEqual(result, Decimal('1.459343570216464550308348164'))

    def test_convert_5USD_to_AUD(self):
        result = self.usd.convert_to(self.aud, Decimal(5))
        self.assertEqual(result, Decimal('7.296717851082322751541740820'))
