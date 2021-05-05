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


url_profile = 'https://ca.finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://ca.finance.yahoo.com/quote/{}/financials?p={}'
url_history = 'https://query1.finance.yahoo.com/v7/finance/download/{}?'

def get_list_500():
    payload = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    first_table = payload[0]
    second_table = payload[1]

    df = first_table
    df.head()
    symbols = df['Symbol'].values.tolist()
    #print(symbols[:15])

    names = df['Security'].values.tolist()
    #print(names[:15])

    sectors = df['GICS Sector'].values.tolist()
    sectors = set(sectors)
    #print(sectors)
    result= df[['Symbol','Security','GICS Sector']]
    return symbols

def get_json_data(stock):
    response = requests.get(url_profile.format(stock, stock))
    soup = BeautifulSoup(response.text, 'html.parser')
    pattern = re.compile(r'\s--\sData\s--\s')
    script_data = soup.find('script', text=pattern).contents[0]

    start = script_data.find("context") - 2
    json_data = json.loads(script_data[start:-12])
    return json_data

def get_closing_price(json_data):
    # Closing Price
    price = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['price']
    last_closing_price = price['regularMarketPreviousClose']['raw']

    return last_closing_price

def get_fiftytwo_high_price(json_data):
    # Summary
    summary_detail = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']

    fiftytwo_high_price = summary_detail['fiftyTwoWeekHigh']['raw']
    return fiftytwo_high_price

def get_stock_desc(json_data):
    summary_detail = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['quoteType']

    desc = summary_detail['shortName']

    return desc



#print(get_max_price("MSFT",2019,2020))
