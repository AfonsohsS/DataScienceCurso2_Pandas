# Relatório de Análise de Dados

## Importando os dados

import pandas as pd

pd.read_csv('aluguel.csv', sep = ';')

dados = pd.read_csv('aluguel.csv', sep = ';')

type(dados)

dados.info()

# Informações gerais sobre a base de dados

dados.dtypes

dataType = pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])

dataType.columns.name = 'Variáveis'

dataType

# Verificando a quantidade de variáveis
dados.shape

print('A base de dados apresenta {} registros e {} variáveis'.format(dados.shape[0], dados.shape[1]))