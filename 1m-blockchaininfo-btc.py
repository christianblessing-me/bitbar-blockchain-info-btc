#!/usr/bin/env python
# coding=utf-8

# <bitbar.title>Blockchain.info BTC-EUR Portfolio Tracker</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Christian M. Blesing</bitbar.author>
# <bitbar.author.github>picturaluce</bitbar.author.github>
# <bitbar.desc>Show BTC-EUR + your portfolio value.</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

# Special thanks goes out to Blockchain for their API: https://www.blockchain.info

import json
import urllib2

# BTC Portfolio amount goes here:
portfolio = 0.07953116

# Set currency here: 
# (USD, AUD, BRL, CAD, CHF, CLP, CNY, DKK, EUR, GBP, HKD, INR, ISK, JPY, KRW, NZD, RUB, SEK, SGD, THB, TWD):
currency = 'EUR'

# Currency symbol selection
if currency == 'USD':
    symbol_currency = '$ '
elif currency == 'AUD':
    symbol_currency = 'A$ '
elif currency == 'BRL':
    symbol_currency = 'R$ '
elif currency == 'CAD':
    symbol_currency = 'C$ '
elif currency == 'CHF':
    symbol_currency = 'CHF '
elif currency == 'CLP':
    symbol_currency = 'CLP$ '
elif currency == 'CNY':
    symbol_currency = '¥ '
elif currency == 'DKK':
    symbol_currency = 'KR '
elif currency == 'EUR':
    symbol_currency = '€ '
elif currency == 'GBP':
    symbol_currency = '£ '
elif currency == 'HKD':
    symbol_currency = 'HK$ '
elif currency == 'INR':
    symbol_currency = '₹ '
elif currency == 'ISK':
    symbol_currency = 'KR '
elif currency == 'JPY':
    symbol_currency = '¥ '
elif currency == 'KRW':
    symbol_currency = '₩ '
elif currency == 'NZD':
    symbol_currency = '$ '
elif currency == 'RUB':
    symbol_currency = '₽ '
elif currency == 'SEK':
    symbol_currency = 'KR '
elif currency == 'SGD':
    symbol_currency = 'S$ '
elif currency == 'THB':
    symbol_currency = '฿ '
elif currency == 'TWD':
    symbol_currency = 'NT$ '
else:
    symbol_currency = 'undefined'

# API URL
api_blockchain = 'https://blockchain.info/de/ticker'

# API Request: Blockchain.info
blockchain_request = urllib2.Request(api_blockchain)
blockchain_response = urllib2.urlopen(blockchain_request).read()
blockchain_result = json.loads(blockchain_response)
temp_blockchain = float(blockchain_result[currency]['last'])
temp_blockchain_str = str(temp_blockchain)

# Calculate Portfolio
portfolio_result = round( (temp_blockchain * portfolio), 2)
portfolio_result_show = str(portfolio_result)

# Output
print(symbol_currency + temp_blockchain_str)
print('---')
print('Portfolio: '+ symbol_currency + portfolio_result_show)