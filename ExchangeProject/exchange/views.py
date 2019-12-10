from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView

from .forms import AddCurrencyForm
from .models import Currency


from bs4 import BeautifulSoup
import requests


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

    # table = soup.find('table')
    # rows = soup.find_all('tr')

    return HttpResponse(soup)
