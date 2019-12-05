from django.urls import path

from . import views


app_name='exchange'
urlpatterns = [
    path('', views.AllCurrenciesListView.as_view(), name='index'),
    path('/calculator/', views.calc_exchange_rates, name='calculator'),
]
