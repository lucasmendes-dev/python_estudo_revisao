import requests
import pprint

key = ""  #coloque aqui sua chave do Alpha Vantage

#para descobrir o código da ação que vc quer, acesse yahoo.finance
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={key}'
r = requests.get(url)
data = r.json()

pprint.pprint(float(data["Time Series (5min)"]["2022-11-08 09:15:00"]["4. close"]))