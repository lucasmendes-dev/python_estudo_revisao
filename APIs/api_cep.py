import requests
import pprint

#localizar endereço pelo CEP
cep = "30.710-260"
cep = cep.replace(".", "").replace("-", "").replace(" ", "") #para o caso de formatar

if len(cep) == 8:
    link = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    valor_cep = link.json()

    #print(valor_cep)
else:
    print("CEP inválido")


#Descobrir CEP pelo endereço passado

uf = "MG"
cidade = "Belo Horizonte"
rua = "Rio Espera"

req = requests.get(f"https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/")   #sempre usar https://
endereco_cep = req.json()

pprint.pprint(endereco_cep)
