from .models import Currency

from django.test import Client, TestCase
from django.urls import reverse


class ExchangeTestClient(TestCase):

    def setUp(self):
        self.client = Client()

    def test_loading_root_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_create_currency(self):
        context = {'full_name': 'test_currency',
                   'currency_abbr': 'TEST',
                   'rate_vs_base': '1'}
        response = self.client.post(reverse('exchange:add_currencies'), context)
        self.assertEqual(response.status_code, 302)
