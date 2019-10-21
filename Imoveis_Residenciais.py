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
