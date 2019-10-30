# Mais sobre Gráficos

import pandas as pd
import matplotlib.pyplot as plt 
plt.rc('figure', figsize = (15, 8))

dados = pd.read_csv('extras/dados/aluguel.csv', sep = ';')

dados.head(10)

# Criando a área que irá receber os gráficos
area = plt.figure()

# Posicionando os gráficos
g1 = area.add_subplot(2, 2, 1)
g2 = area.add_subplot(2, 2, 2)
g3 = area.add_subplot(2, 2, 3)
g4 = area.add_subplot(2, 2, 4)

# Definindo os tipo e dados dos gráficos
g1.scatter(dados.Valor, dados.Area)
g1.set_title('Valor x Area')

g2.hist(dados.Valor)
g2.set_title('Histograma do Valor')

## Criando um grupo de dados aleatório
dados_g3 = dados.Valor.sample(100)

## Refazendo o index
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Amostra Valor')

## Criando um grupo
grupo = dados.groupby('Tipo')['Valor']
labels = grupo.mean().index
valores = grupo.mean().values
g4.bar(labels, valores)
g4.set_title('Média por Tipo')

area.savefig('extras/grafico.png', dpi = 150, bbox_inches = 'tight')
