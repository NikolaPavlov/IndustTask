from django import forms

from .models import Currency


class AddCurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = ('full_name', 'currency_abbr', 'rate_vs_base')
