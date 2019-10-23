
# Formas de Selecao

import pandas as pd 

data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]

# Utilizando o .split() para criar uma lista a partir de uma string
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())
df
df.c1

df[['c3', 'c1']]

df[::-1]

# A partir da linha 'L1'selecionar colunas c3 e c1
df[1:][['c3', 'c1']]

# Com o loc é possível selecionar uma linha pelo rótulo dela
# no lugar de usar o index. Criando uma series com os valores

df.loc['l3']
df.loc[['l3', 'l2']] # seleciona mais de uma

# Posso utilizar uma notacao matricial usando o loc
df

df.loc['l2', 'c3']

# Com iloc você faz a mesma coisa, só que utilizando os indices numericos
df.iloc[1,2]

df.loc[['l3', 'l1'], ['c4','c1']]