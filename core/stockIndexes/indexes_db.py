import re
import json
import csv
import requests
import os
import math
from io import StringIO
from bs4 import BeautifulSoup
import pandas_datareader as web
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils.datetime_safe import date
from pandas_datareader import data as pdr
from .models import *

url_profile = 'https://ca.finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://ca.finance.yahoo.com/quote/{}/financials?p={}'
url_history = 'https://query1.finance.yahoo.com/v7/finance/download/{}?'
"""
def get_max_price(stock, start, end):

    #df = web.DataReader(stock, data_source='yahoo',
    #                    start=start, end=end)

    enddate = datetime(2016, 12, 31)
    today = date.today()
    begdate = today - relativedelta(days=1)
    print(begdate)
    #print(df['Close'].keys())
    mystock = pdr.get_data_yahoo(stock, start=begdate, end=today )
    #mystock = pdr.get_data_yahoo(stock, start=today, end="2021-04-12")
    mystock['high'] = mystock.Close.shift(1).rolling(window=5).max()
    # 5-days low
    mystock['low'] = mystock.Close.shift(1).rolling(window=5).min()
    # 5-days mean
    #mystock['avg'] = mystock.Close.shift(1).rolling(window=5).mean()
    mystock['close'] = mystock.Close
    mystock['long_entry'] = mystock.Close > mystock.high
    mystock['short_entry'] = mystock.Close < mystock.low
    #print(mystock[['high','close','long_entry','short_entry']])
    max_price = mystock.Close.max()


    #print(mystock[['close','high','low','long_entry','short_entry']])

    return(max_price)
"""

def algo_trading_list():
    stocks = Stock.objects.all()
    result = {}
    ranks = rank_stocks()
    for stock in stocks:
        result[stock.name] = {"desc":stock.desc,
                              "closing":stock.closing,
                              "fiftyTwoHigh":stock.fiftyTwoHigh,
                              "priceToFiftyTwoHigh":price_to_fiftytwo_high(stock.closing, stock.fiftyTwoHigh),
                              "rank":ranks[stock.name]
                              }
    return result

def price_to_fiftytwo_high(closing, fiftytwo_high):
    index = (closing - fiftytwo_high) / fiftytwo_high
    return index
def rank_stocks():
    stocks = Stock.objects.all()
    result = {}
    for stock in stocks:
        result[stock.name] = price_to_fiftytwo_high(stock.closing, stock.fiftyTwoHigh)

    res = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
    i = 1
    ranks = {}
    for stock in res:
        ranks[stock]= i
        i+=1
    return ranks

print(rank_stocks())