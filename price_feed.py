#this application is designed to print the prices of different cryptocurrencies on different exchanges
#it is split up into multiple files to make things easier to read and to improve maintainability

import coinbase_api_interface as cb#import the coinbase api interface
import okcoin_api_interface as ok#import the okcoin api interface

###-------------------------------------------------------###
client = cb.new_client()#connect to coinbase
print ("Coinbase BTC-USD: ", cb.get_price(client, 'BTC'))
print ("Coinbase BCH-USD: ", cb.get_price(client, 'BCH'))
print ("Coinbase LTC-USD: ", cb.get_price(client, 'LTC'))
print ("Coinbase ETH-USD: ", cb.get_price(client, 'ETH'))


###-------------------------------------------------------###
print ("OKCoin BTC-USD: ", ok.get_price('BTC'))
print ("OKCoin BCH-USD: ", ok.get_price('BCH'))
print ("OKCoin LTC-USD: ", ok.get_price('LTC'))
print ("OKCoin ETH-USD: ", ok.get_price('ETH'))

