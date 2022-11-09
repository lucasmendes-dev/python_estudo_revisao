import requests
import json

cotacao = requests.get("https://economia.awesomeapi.com.br/json/all")
cotacoes = cotacao.json()
#print(cotacoes["USD"]["bid"])


cotacoes_30d = requests.get("https://economia.awesomeapi.com.br/json/daily/USD-BRL/30")
cotacoes_30d = cotacoes_30d.json()

lista_bid = [float(item["bid"]) for item in cotacoes_30d]  #list comprehension
#print(lista_bid)



bitcoin = requests.get("https://economia.awesomeapi.com.br/json/daily/BTC-BRL/100?start_date=20220101&end_date=20221031")
bitcoin_btc = bitcoin.json()
#print(bitcoin_btc)

lista_btc = [float(item["bid"]) for item in bitcoin_btc]
print(lista_btc)
