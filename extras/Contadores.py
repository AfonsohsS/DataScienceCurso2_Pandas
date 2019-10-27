# Contadores

import pandas as pd 

s = pd.Series(list('asdadeadesdasesda'))
s

# Apresentando os valores sem repetição
s.unique()

# Apresentando a distribuição de frequência dos valores
s.value_counts()

dados = pd.read_csv('extras/dados/aluguel.csv', sep = ';')

dados.Tipo.unique()
dados.Tipo.value_counts()

# EXERCICIOS

# Distribuição de ocorrências
m1 = 'CCcCCccCCCccCcCccCcCcCCCcCCcccCCcCcCcCcccCCcCcccCc'
m2 = 'CCCCCccCccCcCCCCccCccccCccCccCCcCccCcCcCCcCccCccCc'
m3 = 'CccCCccCcCCCCCCCCCCcccCccCCCCCCccCCCcccCCCcCCcccCC'
m4 = 'cCCccCCccCCccCCccccCcCcCcCcCcCcCCCCccccCCCcCCcCCCC'
m5 = 'CCCcCcCcCcCCCcCCcCcCCccCcCCcccCccCCcCcCcCcCcccccCc'

# Criação da Lista de Eventos
eventos = {'m1' : list(m1), 
            'm2' : list(m2),
            'm3' : list(m3),
            'm4' : list(m4),
            'm5' : list(m5)}

# Criando o DF Moedas com a lista de ocorrências
moedas = pd.DataFrame(eventos)

moedas

# Criando o DF df com os indices e Tipos
df = pd.DataFrame(data = ['Cara', 'Coroa'], index = ['c', 'C'], columns = ['Faces'])
df

# Concatenando os DataFrames (moeda e df) no novo df
# Usando o for para percorrer todos os valoes no DF(moedas), para em cada coluna [item]
for item in moedas:
    df = pd.concat([df, moedas[item].value_counts()], 
                    axis = 1, 
                    sort=True)

df