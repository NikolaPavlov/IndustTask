from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView

from .forms import AddCurrencyForm
from .utils import scraper
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
        response_data['result_of_conv'] = round(result_of_conv,2)
        return JsonResponse(response_data)
    else:
        return render(request, 'exchange/calc.html', context)


def scraper_view(request):
    scraper()
    return redirect(reverse('exchange:index'))
