from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from exchange.utils import scraper


class Command(BaseCommand):
    help = 'Refresh the exchange rates from BNB website'

    def handle(self, *args, **kwargs):
        self.stdout.write(scraper())
