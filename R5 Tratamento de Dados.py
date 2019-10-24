# Tratamento de dados faltantes

import pandas as pd 

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')
dados

dados.head(10)

dados.isnull() # Marca True nos nulos

dados.notnull() # Marca True nos não nulos

# Com o método info() conseguimos visualizar informações do DataFrame e
# identificar as variáveis que possuem valores nulos.
dados.info()

# Usando o isnull() para marcar com True os campos nulos
selecao_valor = dados.Valor.isnull()
selecao_valor
dados[selecao_valor]

# Retirando as linhas que possuem campos nulos na variável 'Valor'
# Gravando o resultado no DataFrame com o inplace
dados.dropna(subset = ['Valor'], inplace = True)
dados
