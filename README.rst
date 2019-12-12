########
Exchange
########

+ Index: http://localhost:8000 ---> list all exchange rates + 'Refresh Rates' button on the bottom
+ Calculator: http://localhost:8000/calculator ---> calculating exhcange rates
+ AddCurrency: http://localhost:8000/add_currencies ---> form for adding new currency
+ Custom manage.py refreshrates command ---> refresh the rates from BNB page

How to run
==========

+ Install dependencies - pipenv install --dev
+ python manage.py makemigrations
+ python manage.py migrate
+ add base currency ( Bulgarian Lev : BGN : 1 )

Notes:
======

BNB Exchange Rates:

    + http://bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm
