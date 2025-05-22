#UTILIZANDO O SITE REST COUNTRIES https://restcountries.com/

import requests

pais = "brazil"

url= f'https://restcountries.com/v3.1/name/{pais}'
resposta =  requests.get(url)
dados = resposta.json()

# exibir as infos
info = dados[0]
print(f'Nome: {info['name']['common']}')
print(f'capital: {info['capital'][0]}')
print(f'região: {info['region']}')
print(f'População: {info['population']}')