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

# Fazendo uma análise modular por Grupos +++++
dados.boxplot(['Valor'], by = ['Tipo'])

# Criando uma serie Valor a partir do DataFrameGroupBy
group_type = dados.groupby('Tipo')['Valor']
type(group_type)

# Calculo dos quartis e limites (em format Series de valores)
Q1 = group_type.quantile(.25)
Q3 = group_type.quantile(.75)
IIQ = Q3 - Q1 
lower_limit = Q1 - 1.5 * IIQ
upper_limit = Q3 + 1.5 * IIQ

# Loop para percorrer os Tipos agrupados e aplicar a selecao definida
# criando um novo DataFrame com a concatenação do Tipos e seus valores
# redefinidos com a remoção dos outliers.
dados_new = pd.DataFrame()
for tipo in group_type.groups.keys():
    eh_tipo = dados.Tipo == tipo
    eh_dentro_limite = (dados['Valor'] >= lower_limit[tipo]) & (dados['Valor'] <= upper_limit[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])
    
dados_new.boxplot(['Valor'], by = ['Tipo'])

dados_new.to_csv('aluguel_residencial_w_outliers.csv', sep = ';')