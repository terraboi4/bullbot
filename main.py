
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


def calculate_macd(data, stock):
    # https://medium.com/@financial_python/building-a-macd-indicator-in-python-190b2a4c1777
    data['EMA12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['EMA200'] = data['Close'].ewm(span=200, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    last_row = data.iloc[-1]
    second_last_row = data.iloc[2]

    if second_last_row['MACD'] < second_last_row['Signal_Line'] and last_row['MACD'] > last_row['Signal_Line']:
        print(stock, ' Cross Above Signal Line')
    else:
        print(stock, ': No Crossover')


for stock in stocks:
    data = yf.Ticker(stock).history(period='1mo', interval='1h')
    calculate_macd(data, stock)
