from decimal import Decimal

import requests

from bs4 import BeautifulSoup

from exchange.models import Currency
from ExchangeProject.settings import BNB_URL


def scraper():
    r = requests.get(BNB_URL)
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
                                                         'rate_vs_base': rate_vs_base})

    return 'Refresh completed'


def html_table_body_to_array(table_body):
    # return array with the data of the table
    data = []
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values
    return data[:-1]  # The last row of the table is removed
