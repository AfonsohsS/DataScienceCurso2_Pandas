# Criando Estruturas de Dados

import pandas as pd

data = [1, 2, 3, 4, 5]

s = pd.Series(data)

s

index = ['Linha' + str(i) for i in range(5)]

index

# Criando a serie utilizando os Arrays data e index
s = pd.Series(data, index)

s

# Outra forma de obter o mesmo resultado utilizando dicionário

data = {'Linha' + str(i) : i + 1 for i in range(5)}

s2 = pd.Series(data)

s2

# Você pode fazer operações com as series.

s3 = s2 + 2

s3

s5 = s3 + s2

s5

list_data = [[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]]

new_df = pd.DataFrame(list_data)
new_df

index = ['Linha' + str(i) for i in range(3)]

new_df = pd.DataFrame(list_data, index)
new_df

columns = ['Coluna' + str(i) for i in range(3)]

new_df.columns = columns

new_df

# Usando um dicionáio

data2 = {
        'Coluna0': {'Linha0': 1, 
                    'Linha1': 4, 
                    'Linha2': 7},
        'Coluna1': {'Linha0': 2, 
                    'Linha1': 5, 
                    'Linha2': 8},
        'Coluna2': {'Linha0': 3, 
                    'Linha1': 6, 
                    'Linha2': 9}
        }

data2

new_df2 = pd.DataFrame(data2)

new_df2

# Utilizando uma lista de Tuplas

data_tuplas = [
                (1, 2, 3), 
                (4, 5, 6), 
                (7, 8, 9)
            ]

new_df3 = pd.DataFrame(data = data_tuplas, index = index, columns = columns)

new_df3

# Concatenando DataFrames

new_df
new_df2
new_df3

new_df[new_df > 0] = 'A'
new_df2[new_df2 > 0] = 'B'
new_df3[new_df3 > 0] = 'C'

new_df
new_df2
new_df3

df4 = pd.concat([new_df, new_df2, new_df3])
df4

df5 = pd.concat([new_df, new_df2, new_df3], axis = 1)
df5