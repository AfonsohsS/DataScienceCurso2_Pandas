
# Oraganizando DataFrames (Sort)

import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

df = pd.DataFrame(data, list('321'), list('zyx'))
df

# Organizando as linhas
## O sort_index organiza o índice levando toda a linha junto
df.sort_index(inplace=True)
df

# Com a inclusão (axis = 1) as colunas são reorganizados
df.sort_index(inplace=True, axis = 1)
df

# Organizando o DataFrame pelos valores
df.sort_values(by = 'x', inplace = True)
df.sort_values(by = '3', axis = 1, inplace = True)
df

# Sem usar o argumento inplace o DataFrame não é modificado
df.sort_index()
df.sort_index(axis = 1)
df