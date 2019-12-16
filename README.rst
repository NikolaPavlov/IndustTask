=============
Exchange TASK
=============

Requirements
============

Develop one app Django project - currency exchanger.

+ Ability to add an exchange rates ('US Dollar', 'USD', 1.72)
+ Calculator functionality (calc 'x' amount of USD to EUR)
+ Calculation should happen with AJAX on the web page
+ Django view showing all available exchange rates
+ Management command to pull all rates from BNB website
+ Button sync now on the index page which will pull all rates from BNB website
+ In the end create Pull Reguest (Merge Request) from separate branch with some of the futures

SiteMap
=======

+ Index: http://localhost:8000 ---> list all exchange rates + sync exchange rates button
+ Calculator: http://localhost:8000/calculator ---> calculating exhcange rates between currencies AJAX
+ AddCurrency: http://localhost:8000/add_currencies ---> form for adding new currency


Notes:
======

BNB Exchange Rates Webpage:

    + http://bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm
