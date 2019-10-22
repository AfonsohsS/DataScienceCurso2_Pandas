# Relatório de Análise IV
## Seleção e Frequências

import pandas as pd

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')

dados.head(12)

## Selecione somente os imóveis classificados com tipo 'Apartamento'
selecao = dados.Tipo == 'Apartamento'
selecao
nAp = dados[selecao].shape[0]
nAp

## Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
    ## Quando temos mais de um termo como condição é necessário colocá-los entre parênteses
selecao2 = (dados.Tipo == 'Casa') | (dados.Tipo == 'Casa de Condomínio') | (dados.Tipo == 'Casa de Vila')
selecao2
nCasas = dados[selecao2].shape[0]
nCasas

## Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
    # 60 <= Area <= 100
selecao3 = (dados.Area >= 60) & (dados.Area <= 100) 
nArea = dados[selecao3].shape[0]
nArea

## Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
selecao4 = (dados.Quartos >= 4) & (dados.Valor < 2000.0)
nQuartoAluguel = dados[selecao4].shape[0]
nQuartoAluguel

# Imprimindo o relatório
print("Numero de imóveis classificados com tipo 'Apartamento' -> {}".format(nAp))
print("Numero de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila' -> {}".format(nCasas))
print("Numero de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}".format(nArea))
print("Numero de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00' -> {}".format(nQuartoAluguel))