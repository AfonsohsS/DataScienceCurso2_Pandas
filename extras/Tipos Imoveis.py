# Relatório de Análise II

## Tipos de Imóveis
import pandas as pd

dados = pd.read_csv('aluguel.csv', sep=';')

dados['Tipo']

tipoImovel = dados.Tipo

tipoImovel.drop_duplicates()

## (inplace = True) modifica a variável a partir da execução
## do método, não precisamos criar uma variável e atribuir 
## a execução à ela
tipoImovel.drop_duplicates(inplace = True)

tipoImovel