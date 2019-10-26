# Tratamento de dados faltantes

import pandas as pd 

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')
dados

dados.head(10)

dados.isnull() # Marca True nos nulos

dados.notnull() # Marca True nos não nulos

# Com o método info() conseguimos visualizar informações do DataFrame e
# identificar as variáveis que possuem valores nulos.
dados.info()

# Usando o isnull() para marcar com True os campos nulos
selecao_valor = dados.Valor.isnull()
selecao_valor
dados[selecao_valor]

# Retirando as linhas que possuem campos nulos na variável 'Valor'
# Gravando o resultado no DataFrame com o inplace
dados.dropna(subset = ['Valor'], inplace = True)
dados

# Tratamento de dados faltantes - Parte II
filtro = dados.Condominio.isnull() 
dados[filtro].shape[0] # 1813 valores nulos

## Filtrando dados com condicionais
selecao = (dados.Tipo == 'Apartamento') & (dados.Condominio.isnull())

# Com o ~ invertemos a seleção boleana, fazendo com que o filtro seja
# invertido e no lugar de selecionar os valores que atendem o filtro,
# ele seleciona os valores que não atendem.
dados = dados[~selecao]

dados

# Com o método fillna() atribuimos valores aos valores nulos
dados[filtro].shape[0] # 1068 Valores nulos

dados.fillna(0) # Solução 1: Substitui todos os valores nulo por 0

dados

dados = dados.fillna({'Condominio' : 0, 'IPTU' : 0})
# Solução 2: A solução acima substitui os valores nulos de forma seletiva
# definindo os valores específicos por variável. 

dados.info() # Conferindo se todos os valores nulos foram removidos

# Exportando o novo BD com a correção dos valores nulos
dados.to_csv('aluguel_residencial.csv', sep = ';', index = False)

