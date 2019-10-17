# Relatório de Análise de Dados

## Importando os dados

import pandas as pd

pd.read_csv('aluguel.csv', sep = ';')

dados = pd.read_csv('aluguel.csv', sep = ';')

type(dados)

dados.info()