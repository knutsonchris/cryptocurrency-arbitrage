#okcoin api interface

import urllib.request#to request information from okcoin's RESTapi
import json#to decode the RESTapi's bytes object response as a string dictionary

def get_price(desired_currency):
	#this function is designed to respond to the client's request of a currency price
	#the function accepts the desired currency
	#the desired currency is then represented in the currency code that the api is expecting
	#the function returns the current price in USD
	
	if desired_currency == 'BTC':
		currency_code = 'btc_usd'
	if desired_currency == 'BCH':
		currency_code = 'bch_usd'
	if desired_currency == 'LTC':
		currency_code = 'ltc_usd'
	if desired_currency == 'ETH':
		currency_code = 'eth_usd'
	
	#now we need to craft our request
	#we will start with the ticker request url and append our desired currency code to the end
	okcoin_restapi_url = "https://www.okcoin.com/api/v1/ticker.do?symbol="
	appended_restapi_url = "".join((okcoin_restapi_url,currency_code))#join the two with no space
	rest_responce = urllib.request.urlopen(appended_restapi_url).read()#send the request
	rest_responce = json.loads(rest_responce.decode('utf-8'))#decode the returned bytes object as a string dict
	rest_responce = (rest_responce['ticker'])#isolate the ticker price information
	amount = rest_responce['last']#isolate the ticker's 'last price' element
	return (amount)