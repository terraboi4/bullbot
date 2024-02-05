
from dotenv import load_dotenv
import os
import requests
from finviz.screener import Screener

print('####### BULL BOT #######')
load_dotenv()
TAAPI_KEY = os.getenv('TAAPI_KEY')
# all stocks to look at
stocks = ['AAPL', 'AMZN', 'NFLX', 'AMD', 'NVDA', 'META',
          'AIP', 'ADMA', 'TSLA', 'DIS', 'GOOG', 'MSFT', 'COST', 'V']
print('Stocks: ', stocks)
finviz_stocks = Screener(filters=None, signal='Channel up')
print(finviz_stocks[1:10])
