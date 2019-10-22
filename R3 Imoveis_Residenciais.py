# Relatório de Análise III
## Filtrando dados - Imoveis Residenciais
import pandas as pd

dados = pd.read_csv('aluguel.csv', sep = ';')

dados

list(dados.Tipo.drop_duplicates())

residencial = [
                'Quitinete',
                'Casa',
                'Apartamento',
                'Casa de Condomínio',
                'Casa de Vila',
            ]

# Definie um boleano para indetificar as linhas que coincidem com nossa seleção
selecao = dados.Tipo.isin(residencial)

# Redefinimos nosso DataFrame para conter apenas os imoveis da seleção
dados_residencial = dados[selecao]

dados_residencial.head(12)

# Conferimos se o filtro foi aplicado corretamente
list(dados_residencial.Tipo.drop_duplicates())

dados_residencial.shape[0] # Devolve o tamanho do DataFrame

# Reconstruimos o index para o novo DataFrame
dados_residencial.index = range(dados_residencial.shape[0])

dados_residencial.head(20)

# Solução do exercício de fixação
# =====================================================

numeros = [i for i in range(11)]
letra = [chr(i + 65) for i in range(11)]
nome_coluna = ['N']
df_teste = pd.DataFrame(data = numeros, 
                        index = letra, 
                        columns = nome_coluna)
df_teste

selecao = df_teste.N.isin([i for i in range(11) if i % 2 == 0])

selecao

df_teste[selecao]
# ====================================================

# Exportando a Base de Dados Filtrada

# Use o index = False para não exporta o index anterior para o novo arquivo
dados_residencial.to_csv('aluguel_residencial.csv', sep = ';', 
                                                    index = False)