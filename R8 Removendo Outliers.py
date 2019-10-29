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
