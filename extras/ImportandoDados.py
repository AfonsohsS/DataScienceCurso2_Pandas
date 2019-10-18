# Módulo Extra - Importando dados

import pandas as pd

# Lendo e visualizando um arquivo Json
json = open('extras/dados/aluguel.json')
print(json.read())

df_json = pd.read_json('extras/dados/aluguel.json')
df_json

# Lendo e visualizando um arquivo txt
txt = open('extras/dados/aluguel.txt')
print(txt.read())

df_txt = pd.read_table('extras/dados/aluguel.txt')
df_txt

# Lendo e visualizando um arquivo Excel xlsx
df_xlsx = pd.read_excel('extras/dados/aluguel.xlsx')
df_xlsx

# Lendo e visualizando dados de uma tabela numa página html
df_html = pd.read_html('extras/dados/dados_html_1.html')
df_html
df_html[0] # Pegando o conteúdo da tabela e exibindo como DataFrame

# Usando um enederço na internet para capturar uma tabela de dados
df_html2 = pd.read_html('https://unafiscosaude.org.br/site/tabelas-de-precos-dos-planos-ativos-para-comercializacao/')
df_html2[0]

# Lendo mais de uma tabela numa página na internet
df_html3 = pd.read_html('https://www.federalreserve.gov/releases/h3/current/default.htm')
df_html3[1]

