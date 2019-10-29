# Exercício Aula 09

import pandas as pd 

dados = pd.read_csv('exercicios/aluguel_amostra_aula09.csv', sep = ';')

valorM2 = dados['Valor m2']

Q1 = valorM2.quantile(.25)
Q3 = valorM2.quantile(.75)
IIQ = Q3 - Q1
lower_limit = Q1 - 1.5 * IIQ
upper_limit = Q3 + 1.5 * IIQ

