# Criando novas variáveis

import pandas as pd 

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')
dados

## Criando variável Valor Bruto
dados['Valor Bruto'] = dados.Valor + dados.Condominio + dados.IPTU 

dados['Valor m2'] = dados.Valor / dados.Area 

# Limitando a duas varáveis
dados['Valor m2'] = dados['Valor m2'].round(2)

dados['Valor Bruto m2'] = (dados['Valor Bruto'] / dados.Area).round(2)

dados.shape

# Unificando casas em uma única variável
dados.Tipo.drop_duplicates() # Identificando os tipos

casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']

# Com o metodo lambda usamos o if para aplicar a String 'Casa' 
# aos valores contidos na variável (casa), e para os demais 
# aplicar (Apartamento)
dados['Grupos'] = dados.Tipo.apply(lambda x: 'Casa' if x in casa else 'Apartamento')

dados

# Excluindo Varíavel

## Exemplos +++++++++++++++++++

# Criando um DataFrame com variáveis de outro DataFrame
dados_aux = pd.DataFrame(dados[['Grupos', 
                                'Valor m2', 
                                'Valor Bruto', 
                                'Valor Bruto m2']])

dados_aux

# Deletando Varíavel - Opção 1
del dados_aux['Valor Bruto m2']

# Deletando Varíavel - Opção 2
dados_aux.pop('Valor m2')

# Deletando Varíavel - Opção 3
dados_aux.drop(['Valor Bruto'], axis = 1, inplace = True)

dados_aux
# ++++++++++++++++++++++++++++++

dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis = 1, inplace = True)

dados

# Atualizando arquivo BD
dados.to_csv('aluguel_residencial.csv', sep = ';', index = False)