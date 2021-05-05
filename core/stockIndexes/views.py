from django.shortcuts import render
from .indexes_db import *
#from .models import *
# Create your views here.
def stock_table(request):

    context = {}
    stock_table = algo_trading_list()
    keys = stock_table.keys()
    values = stock_table.values()
    context['keys'] = keys
    context['values'] = values
    context['json_pretty'] = stock_table
    return render(request, 'stock_table.html', context)