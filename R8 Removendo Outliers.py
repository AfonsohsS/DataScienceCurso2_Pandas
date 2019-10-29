# Identificando e Removendo Outliers

import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')
dados.head(10)

# Construindo um box plot
dados.boxplot(['Valor'])

# Exibir os principais valores outliers
dados[dados.Valor >= 500000]

# Criar uma series com os valores
valor = dados.Valor 

# Calculo dos quartis e limites
Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1 
lower_limit = Q1 - 1.5 * IIQ
upper_limit = Q3 + 1.5 * IIQ

# Definindo a seleção
selecao = (valor >= lower_limit) & (valor <= upper_limit)

# Aplicando filtro selecionado
selected_data = dados[selecao]
selected_data.boxplot(['Valor'])
selected_data.hist(['Valor'])