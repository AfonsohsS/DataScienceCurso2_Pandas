# Criando Faixas de Valor

import pandas as pd 

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')
dados.head(10)

# Contar números de quartos
# De 1 a 2
# De 3 a 4
# De 5 a 6
# 7 ou mais

# Inicia com o limite inferior (0) e depois insere os limites 
# superiores de cada faixe.
classes = [0, 2, 4, 6, 100]

quartos = pd.cut(dados.Quartos, classes)

quartos

pd.value_counts(quartos)

# Exemplo de resposta para o comando acima
# (0, 2]      11250
# (2, 4]       9681
# (4, 6]        686
# (6, 100]       50
# Name: Quartos, dtype: int64

labels = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 ou mais quartos']

# Adicionando labels as faixas
quartos = pd.cut(dados.Quartos, classes, labels=labels)

pd.value_counts(quartos)

# Exemplo de resposta para o comando acima
# 1 e 2 quartos        11250
# 3 e 4 quartos         9681
# 5 e 6 quartos          686
# 7 ou mais quartos       50
# Name: Quartos, dtype: int64

# Incluindo o valor mais baixo
quartos = pd.cut(dados.Quartos, classes, labels=labels, include_lowest=True)
pd.value_counts(quartos)