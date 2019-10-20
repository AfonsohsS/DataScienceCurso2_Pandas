# Relatório de Análise II

## Tipos de Imóveis
import pandas as pd

dados = pd.read_csv('aluguel.csv', sep=';')

dados['Tipo']

tipoImovel = dados.Tipo

type(tipoImovel)

tipoImovel.drop_duplicates()

## (inplace = True) modifica a variável a partir da execução
## do método, não precisamos criar uma variável e atribuir 
## a execução à ela
tipoImovel.drop_duplicates(inplace = True)

## Oraganizando a visualização

tipo_de_imovel = pd.DataFrame(tipoImovel)
tipo_de_imovel

tipo_de_imovel.shape[0]

## Reorganizando o index do DataFrame

tipo_de_imovel.index = range(tipo_de_imovel.shape[0])

tipo_de_imovel.index

tipo_de_imovel.columns.name = "id"

tipo_de_imovel