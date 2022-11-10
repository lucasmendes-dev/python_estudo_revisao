import requests
import pprint

link = requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/4112/periodos/2006/variaveis/2586?localidades=N1[all]")
link = link.json()

pprint.pprint(link[0]["resultados"][0]["series"])