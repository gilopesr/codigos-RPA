import requests
# import sys
# import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

codigo = 'BR'
url = f'https://restcountries.com/v3.1/alpha/{codigo}'

reposta = requests.get(url)
dados = reposta.json()

info = dados[0]
print(f'Pais: {info['name']['common']}')
print(f'Moeda: {list(info['currencies'].keys())[0]}')