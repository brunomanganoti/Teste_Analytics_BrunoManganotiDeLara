# Script dedicado a geração dos dados fictícios, limpeza dos dados e geração do arquivo .csv dos dados limpos.
""" 
- Crie um script para simular um dataset de vendas com pelo menos 50 registros, contendo as colunas: 
  {ID, Data, Produto, Categoria, Quantidade, Preço}. 
- O período dos dados deve ser de 01/01/2023 a 31/12/2023.
- Realize a limpeza dos dados, incluindo tratamento de valores faltantes, remoção de duplicatas e 
conversão de tipos de dados, se necessário. 
- Salve o dataset limpo em um arquivo data_clean.csv. 
"""

# Importação das bibliotecas e arquivos
from map_produto_cat_preco import produto_cat_preco
from faker import Faker
from datetime import date
import pandas as pd
import numpy as np
import random

faker = Faker('pt_BR') # Gera instância de um objeto faker configurado para o idioma Português - BR
num_registros = 65     # Define o número de registros a serem criados

# Variáveis de controle para geração de datas no formato date
data_inicial = date(2023,1,1)   # Início: 01/01/2023 
data_final   = date(2023,12,31) # Fim...: 31/12/2023 

# Função utilizada para gerar um registro do dataframe
def gera_df(tamanho):
    # Inicia lista de vendas
    vendas = []

    for idx in range(1, num_registros+1):
        produto = random.choice(list(produto_cat_preco.keys()))
        categoria, preco = produto_cat_preco[produto]
        vendas.append({
            'ID': idx,
            'Data': faker.date_between(start_date=data_inicial, end_date=data_final),
            'Produto': produto,
            'Categoria': categoria,
            'Quantidade': random.randint(1,100),
            'Preço': preco
        })

    # Transforma os registros gerados em dataframe
    df = pd.DataFrame(vendas, columns=['ID','Data','Produto','Categoria','Quantidade','Preço'])
    return df

# Armazena o dataframe gerado em 'df_vendas'
df_vendas = gera_df(num_registros)

# Adiciona valores nulos a linhas aleatórias do dataframe
# Como os preços são fixos por produto, adiciona valores nulos a quantidade apenas
for _ in range(25):
    idx = random.randint(0, len(df_vendas)-1) 
    coluna = random.choice(['Quantidade'])
    df_vendas.at[idx, coluna] = pd.NA

# Adiciona linhas duplicadas para simulação de limpeza dos dados
linhas_duplicadas = df_vendas.sample(25)                                 # Pega 25 linhas aleatórias do dataframe gerado
df_vendas = pd.concat([df_vendas, linhas_duplicadas], ignore_index=True) # Concatena as linhas escolhidas (duplicadas)

# Retire o comentário do bloco abaixo para visualização do dataframe após o tratamento dos dados
"""
print('\n-----------------------------')
print('DADOS GERADOS (FORMATO BRUTO)\n')
print(df_vendas.to_string(index=False))
"""

# ===== TRATAMENTO E LIMPEZA DE DADOS ===== #
# -- REMOVE DUPLICATAS -- # 
df_vendas.drop_duplicates(inplace=True)

# -- TRATA VALORES NULOS/VAZIOS -- #
# Preenche os campos nulos da coluna de Quantidade com a mediana da mesma
df_vendas['Quantidade'] = df_vendas['Quantidade'].fillna(df_vendas['Quantidade'].median())

# Retire o comentário do bloco abaixo para visualização do dataframe após o tratamento dos dados
""" 
print('\n----------------------------------')
print('APÓS TRATAMENTO E LIMPEZA DE DADOS\n')
print(df_vendas.to_string(index=False)) 
"""

# Salva o dataframe limpo no arquivo .csv
df_vendas.to_csv('data_clean.csv', index=False)

# Carrega o dataset limpo do arquivo .csv
df_vendas_clean = pd.read_csv('data_clean.csv')

# Cria uma nova coluna realizando o cálculo do total de vendas (Quantidade x Preço)
df_vendas_clean['total_vendas'] = round((df_vendas_clean['Quantidade'] * df_vendas_clean['Preço']), 2)

# Atualiza o arquivo .csv com a coluna adicionada
df_vendas_clean.to_csv('data_clean.csv', index=False)

# Retire o comentário do bloco abaixo para visualização do dataframe após o cálculo e adição da coluna 
# com o total de vendas (total_vendas)
""" 
print('\n-------------------------------')
print('APÓS CÁLCULO DO TOTAL DE VENDAS\n')
print(df_vendas_clean.to_string(index=False)) 
"""