import krakenex
from pykrakenapi import KrakenAPI
import time
import decimal
import json
7k
KrakenAPI(kraken_api)
8 #df, lastk.get_ohlc_data("BCHUSD", ascending=True)
def now():
decimal.Decimal(time.time())
def get_balance():
with open('balance.json', '') as fi
return json.load(f)
except:
#change this for the actual query to the database once the script is working return 'ZUSD 1000.0', 'EUR. HOLD": "0.0000"}
#print(k.query_private('Balance')['result'])
#return k.query_private('Balance')['result']
update_balance(amount, name, price, sold):
balance get balance()
balance.pop(name[1-4], None)
balance['ZUSD'] = str(float (balance['ZUSD']) amount price)
balance['ZUSD'] = str(float (balance['ZUSD']) (amount price)) balance[name[1-4]] = str(amount)
save_balance(balance)
balance
def save_balance(data):
with open('balance.json', 'w') as fi
json.dump(data, f, indent-4)
get the price data for the crypto
40 def get_crypto_data(pair, since):
ret k.query_public('OHLC', data = ['pair': pair, "since': since}) ret['result'][pair]
get_purchasing price(name):
trades = load_trades()
trades[name][-1]['price_usd']
def load_trades():
trades = {}
with open('trades.json', '') f1
trades = json.load(f)
excepti
crypto pairs:
trades[crypto] = []
return trades
def save_crypto_data(data):
with open('data.json', 'w') as fi json.dump(data, f, indent)
def load_crypto_data_from_file():
data = {}
with open('data.json', '') as f: try:
data = json.load(f)
except:
data = make_crypto_data(data)
save_crypto_data(data)
return data
def make_crypto_data(data):
for name get_pairs()
data[name] = {
'high': [],
'low': [],
'close': [],
'prices': []
return data
save_trade(close, name, bought, sold, amount): saves trades to json file
trade -
'time_stamp': str(int(time.time())),
'price usd close,
'bought bought,
'sold' sold,
'amount': amount
print('TRADE:')
print(json.dumps (trade, indent-4))
trades load_trades()
trades [name].append(trade)
114
price
amount float (balance[name:-4]])
balance update balance (amount, name, price, True)
119
128
120
save trade(price, name, False, True, amount) print('sell')
122
123 def clear_crypto_data(name)
124
data= load_crypto_data_from_file()
for key data[name]:
data[name][key] delete_entries (data[name], key)
save_crypto_data(data)
delete_entries (data, key):
138
139
139
140
142
145
146
14/
149
trades
153
152
154
157
159
else:
160
161
129 130
clean_array[]
for entry data[key][-10:]
clean_array.append(entry)
return clean_array
get_available funds():
balance get_balance()
money = float(balance['ZUSD'])
cryptos not owned G (len(balance)-2)
fundssoney cryptos_not_owned
144 def bot (since, k, pairs):
True:
#comment out to track the same "since" #sinceret['result']['last')
pairs:
If len(trades[pair]) > 0:
# check if we should buy
if trades[pair][-1]['bought']:
#check if we should sell
check_data(pair, crypto_data, False)
crypto_data = get_crypto_data(pair, since) check_data(pair, crypto_data, True)
time.sleep(20)
with open('trades.json', 'w') json.dump(trades, f, indent)
100 de buy_crypto(crypto_data, name):
executes trade
analysis_data= clear_crypto_data(name)
#make sure to make the trade before the next line of code
can buy for
float(crypto_data[-1][4])
101
101 103
Brind
price
106
funds
187
108
189
118
save trade(price, name, True, false, amount) print('buy')
get_available funds()
107 amount funds (1 / price)
136
balance update balance (amount, name, price, False) #amount get_balance()[name [1-4]]
sell_crypto(crypto_data, name);
balance get_balance()
analysis data clear_crypto_data(name)
float(crypto_data[-1][4])
193 def try buy (data, name, crypto_data):
194
195
196
197 198
#analyse the data to see if it is a good opportunity to buy make_trade check_opportunity (data, name, False, True) if make trade:
buy_crypto(crypto_data, name)
199 def check_opportunity(data, name, sell, buy):
# calculate percentage increase of each point count
previous_value = 0
trends. []
for mva in data['close'][-10:]:
if previous_value == 0:
previous_value = mva
else:
if mva/previous_value > 1: # uptrend
if count < 1:
else:
count = 1
count += 1
trends.append('UPTREND')
elif mva/previous_value < 1:
trends.append('DOWNTREND')
if count > 0:
count = -1
else:
count 1
trends.append('NOTREND')
else:


previous_value = mva

#print (trends)

areas = []


area 0




load_trades()


crypto_data = get_crypto_data(pair, since)

if trades[pair][-1]["sold"]
trades[pair][-1] == None:

check_data(pair, crypto_data, True)




if buy:






16





 def check_data(name, crypto_data, should_buy):
TODO: don't repeat-print if list too short high = 0

return False



crypto_data[-1001]:
ava[name]['prices']: ava[name]['prices').append(b)
high+= float(b[2])

low float(b)
close float(b[4])

#085|||| FIX THIS


every moving average into the same array
va[name]['high'].append(high / 100)
Eva[name]['low').append(low / 100)

ava[name]['close').append(close/100)
Sprint (name)
save_crypto_data(va)
#print(json.dumps (ava, indent-4))
1 should buy!
try_buy (eva[name], name, crypto_data)
try_sell(va[name], name, crypto_data)
for mva in reversed(data['close'][-5:]):
price = float(data['prices'][-1][3])
if sell:
purchase_price = float(get_purchasing_price(name)) if price >= (purchase_price* 1.02): print('Should sell with 10% profit')
return True
if price < purchase_price:
print('Selling at a loss')
return True
areas.append(mva / price)
counter 0
if count >= 5:
for area in areas:
counter area
if counter / 3 >= 1.05: return True
def try sell (data, name, crypto_data):
#analyse the data to see if it is a good opportunity to sell

make_trade = check_opportunity(data, name, True, False)
if make trade:
sell_crypto(crypto_data, name)
def get_pairs():
return ['XETHZUSD', 'XXBTZUSD', 'MANAUSD', 'GRTUSD', 'LSKUSD', 'SCUSD'] 258_name_ ___main__':
k = krakenex.API()
k.load_key('kraken.key")
pairs = get_pairs()
since str(int(time.time() - 43200))
mva = load_crypto_data_from_file()
bot (since, k, pairs)

