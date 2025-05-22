# 0-  importação das bibliotecas
import requests
import sqlite3

# eliminar os caracteres especiais
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1- coletar os dados;
pais = 'japan'
url = f'https://restcountries.com/v3.1/name/{pais}'
resposta = requests.get(url)
dados  = resposta.json()

info = dados[0]
nome = info ['name']['common']
capital = info['capital'][0] if 'capital' in info else 'N/A'
regiao = info['region']
populacao = info['population']

print('Dados extraídos da API')
print(f'Nome: {nome}')
print(f'Capital: {capital}')
print(f'Região: {regiao}')
print(f'População {populacao}')

# 2- criação e a conexão com bd(sqlite);
conexao = sqlite3.connect('paises.db')
cursor = conexao.cursor()

# 2.1 criação da tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS paises(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               capital TEXT,
               regiao TEXT,
               populacao TEXT
               )
''')

# 3- inserção de dados;
cursor.execute('''
    INSERT INTO paises(nome, capital, regiao, populacao)
    VALUES(?, ?, ?, ?)
''', (nome, capital, regiao, populacao))
conexao.commit()

# 4- consultar o bd
print('\n Dados inseridos no banco: ')
cursor.execute('SELECT * FROM paises WHERE nome = ?',(nome,))
for linha in cursor.fetchall():
    print(linha)

# Fechar conexao com o bd
conexao.close()