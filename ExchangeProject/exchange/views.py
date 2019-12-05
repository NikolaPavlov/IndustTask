from django.shortcuts import HttpResponse, render
from django.views.generic.list import ListView

from .models import Currency


# def index(request):
#     all_rates = Currency.objects.all()
#     return HttpResponse(all_rates)

class AllCurrenciesListView(ListView):
    model = Currency
    # paginate_by = 2
    context_object_name = 'currencies'
    template_name = 'exchange_calc/index.html'
