from django.core.management.base import BaseCommand, CommandError
from stockIndexes.models import *


class Command(BaseCommand):
    test = 0

    def _get_stock(self):
        tests = Stock.objects.all()
        for i in tests:
            print(i.name + '|' + i.desc + '|' + str(i.fiftyTwoHigh))




    def handle(self, *args, **options):
        self._get_stock()