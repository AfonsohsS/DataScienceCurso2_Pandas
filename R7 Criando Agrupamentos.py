# Criando Agrupamentos

import pandas as pd 

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')
dados.head(10)

dados.Valor.mean()

## Link para cheatSheet de funções estatísticas do panda
## https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#computations-descriptive-stats

# Buscando o valor médio por bairros

bairros = ['Barra da Tijuca', 
            'Copacabana', 
            'Ipanema', 
            'Leblon', 
            'Botafogo', 
            'Flamengo', 
            'Tijuca']

# Criando uma seleção com os valores de bairros selecionados
selecao = dados.Bairro.isin(bairros)

# Criando um DataFrame com os bairros selecionados
dados = dados[selecao]

# Checando os valores com os bairros selecionados
dados.Bairro.unique()

# Criando grupos por bairros
grupo_bairro = dados.groupby('Bairro')
type(grupo_bairro)

grupo_bairro.groups

# Avaliando os valores agrupados
# Com o agrupamento cada bairro é guardado em um DataFrame
for bairro, data in grupo_bairro:
    print('{} -> {}'.format(bairro, data.Valor.mean()))

# Uma forma mais simples de receber a média
grupo_bairro.Valor.mean().round(2)

# Utilizando duas variáveis
grupo_bairro[['Valor', 'Condominio']].mean().round(2)

# ==============================================================
# EXERCÍCIO

alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

alunos

# Obter um DataFrame com as notas médias dos alunos, com duas casas decimais, segundo seu sexo.

sexo = alunos.groupby('Sexo')
sexo = pd.DataFrame(sexo.Notas.mean().round(2))
sexo.columns = ['Notas Médias']
sexo

# =============================================================

# Estatística Descritiva
grupo_bairro.Valor.describe().round(2)

# Selecionando valores estatísticos específicos
grupo_bairro.Valor.aggregate(['min', 'max', 'sum', 'mean'])

# Organizando o DataFrame
grupo_bairro.Valor.aggregate(['min', 
                                'max', 
                                'sum', 
                                'mean']).rename(columns = {'min': 'Minimo', 
                                                            'max': 'Maximo', 
                                                            'sum': 'Soma', 
                                                            'mean': 'Média'})

# Visualizando os dados graficamente

import matplotlib.pyplot as plt
plt.rc('figure', figsize = (20,10))

grupo_bairro['Valor'].std().plot.bar(color = 'green')

# Configurando um gráfico de barras 
fig = grupo_bairro['Valor'].mean().plot.bar(color = 'cyan')
fig.set_ylabel('Valor Aluguel', {'fontsize' : 12})
fig.set_title('Valor Médio do Aluguel', {'fontsize' : 22})