from django.shortcuts import HttpResponse, render
from django.views.generic.list import ListView

from .models import Currency


class AllCurrenciesListView(ListView):
    model = Currency
    # paginate_by = 2
    context_object_name = 'currencies'
    template_name = 'exchange/index.html'


def calc_exchange_rates(request):
    currencies = Currency.objects.all()

    try:
        amount_to_conv = request.GET['amount_to_conv']
        from_curr = Currency.objects.get(currency_abbr=request.GET['from_currency'])
        to_curr = Currency.objects.get(currency_abbr=request.GET['to_currency'])
        result_of_conv = from_curr.convert_to(currency=to_curr, amount=amount_to_conv)
        context = {
            'currencies': currencies,
            'result_of_conv': result_of_conv,
        }
    except:
        context = {
            'currencies': currencies,
        }

        return render(request, 'exchange/calc.html', context)


    return render(request, 'exchange/calc.html', context)
