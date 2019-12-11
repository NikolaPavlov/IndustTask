from decimal import Decimal

import requests

from bs4 import BeautifulSoup

from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView

from .forms import AddCurrencyForm
from .models import Currency


class AllCurrenciesListView(ListView):
    model = Currency
    context_object_name = 'currencies'
    template_name = 'exchange/index.html'


def add_currencies(request):
    if request.method == 'POST':
        form = AddCurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('exchange:index'))
    else:
        form = AddCurrencyForm()
    return render(request, 'exchange/add_currencies.html', {'form': form})


def calc_exchange_rates(request):
    currencies = Currency.objects.all()
    context = {
        'currencies': currencies
    }

    if request.is_ajax():
        amount_to_conv = request.GET['amount']
        from_curr = get_object_or_404(Currency, currency_abbr=request.GET['from_currency'])
        to_curr = get_object_or_404(Currency, currency_abbr=request.GET['to_currency'])

        result_of_conv = from_curr.convert_to(currency=to_curr, amount=amount_to_conv)

        response_data = {}
        response_data['result_of_conv'] = result_of_conv
        return JsonResponse(response_data)
    else:
        return render(request, 'exchange/calc.html', context)


def scraper(request):
    url = 'http://bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm'
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, "html.parser")

    table = soup.find('table', attrs={'class': 'table'})
    table_body = table.find('tbody')
    currency_data = html_table_body_to_array(table_body)

    for row in currency_data:
        rate_vs_base = Decimal(row[3])

        quantity = int(row[2])
        if quantity != 1:
            rate_vs_base = rate_vs_base / quantity

        obj, created = Currency.objects.update_or_create(full_name=row[0],
                                                         currency_abbr=row[1],
                                                         defaults={
                                                            'rate_vs_base': rate_vs_base
                                                         })

    return redirect(reverse('exchange:index'))


def html_table_body_to_array(table_body):
    # return array with the data of the table
    data = []
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values
    return data[:-1]  # The last row of the table is removed
