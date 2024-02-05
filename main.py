
from dotenv import load_dotenv
import os
import yfinance as yf


print('####### BULL BOT #######')
load_dotenv()
TAAPI_KEY = os.getenv('TAAPI_KEY')
# all stocks to look at
stocks = ['AAPL', 'AMZN', 'NFLX', 'AMD', 'NVDA', 'META',
          'AIP', 'ADMA', 'TSLA', 'DIS', 'GOOG', 'MSFT', 'COST', 'V']
print('Stocks: ', stocks)


def calculate_macd(data):
    data['EMA12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
