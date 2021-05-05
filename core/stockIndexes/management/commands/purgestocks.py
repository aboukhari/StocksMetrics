from django.core.management.base import BaseCommand, CommandError
from stockIndexes.models import *


class Command(BaseCommand):
    test = 0

    def _purge_stock(self):
        Stock.objects.all().delete()
        print(Stock.objects.all())




    def handle(self, *args, **options):
        self._purge_stock()