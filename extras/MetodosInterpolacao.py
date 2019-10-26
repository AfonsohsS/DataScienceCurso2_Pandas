

import pandas as pd 

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
data
s = pd.Series(data)
s.fillna(0)

# Interpolando com o fffill

## Preenche os valores nulos repetindo o ultimo
## valor válido encontrado de cima para baixo
s.fillna(method='ffill')

# Interpolando com o bffill

## Preenche os valores nulos repetindo o ultimo
## valor válido encontrado de baixo para cima
s.fillna(method='bfill')

# Interpolando com o .mean()

## Preenche os valores nulos colocando a média
## de todos os valores válidos
s.fillna(s.mean())

# Interpolando com o fffill com limite

## Preenche os valores nulos repetindo o ultimo
## valor válido encontrado de cima para baixo, na
## quantidade de vezes indicada no limit
s.fillna(method='ffill', limit=1)

