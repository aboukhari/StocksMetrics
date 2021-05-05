from django.core.management.base import BaseCommand, CommandError
from stockIndexes.models import *
from stockIndexes.indexes import *


class Command(BaseCommand):
    test = 0

    def _create_stock(self):
        list_fivehundred = get_list_500()

        print(len(list_fivehundred))
        for mystock in list_fivehundred:
            try:
                stock = Stock(name=mystock)
                print(mystock)
                json_data = get_json_data(mystock)
                stock.fiftyTwoHigh = get_fiftytwo_high_price(json_data)
                stock.closing = get_closing_price(json_data)
                stock.desc = get_stock_desc(json_data)
                print(stock.desc)
                stock.save()
            except Exception:
                pass


        print('this')


    def handle(self, *args, **options):
        self._create_stock()