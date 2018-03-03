#coinbase api interface
#note this code expects to find a valid coinbase api key and api secret stored in the current working directory named 'api_key.txt' and 'api_secret.txt'
#in its current form it will crash if it cannot find these files

from coinbase.wallet.client import Client

def new_client():
	#this function is designed to create a new client object, pulling the api key
	#and secret from the corresponding text files. returnes the client object
	
	#fetch the api key from corresponding txt file
	inputfile = open('api_key.txt', 'r')#open the input file
	API_KEY = inputfile.read()#place the text in a string
	inputfile.close()#close the file
	
	#fetch the api secret from corresponding txt file
	inputfile = open('api_secret.txt', 'r')#open the input file
	API_SECRET = inputfile.read()#place the text in a string
	inputfile.close()#close the file

	client = Client(API_KEY, API_SECRET)#create a new client object
	return(client)#return the client to the client application

def get_price(client, desired_currency):
	#this function is designed to respond to the clients request for a currency price
	#the function accepts a client with which to make the request and a desired currency
	#the desired currency is then represented in the format that the api is expecting
	#the function returns the current price in USD
	
	if desired_currency == 'BTC':
		currency_code = 'BTC-USD'
	if desired_currency == 'BCH':
		currency_code = 'BCH-USD'
	if desired_currency == 'LTC':
		currency_code = 'LTC-USD'
	if desired_currency == 'ETH':
		currency_code = 'ETH-USD'
	
	amount = client.get_buy_price(currency_pair = currency_code).amount #send the request
		
	return (amount)
	
	
