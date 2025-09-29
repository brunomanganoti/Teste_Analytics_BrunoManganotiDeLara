# Script dedicado a geração dos dados fictícios, limpeza dos dados e geração do arquivo .csv dos dados limpos.
""" 
- Crie um script para simular um dataset de vendas com pelo menos 50 registros, contendo as colunas: 
  {ID, Data, Produto, Categoria, Quantidade, Preço}. 
- O período dos dados deve ser de 01/01/2023 a 31/12/2023.
- Realize a limpeza dos dados, incluindo tratamento de valores faltantes, remoção de duplicatas e 
conversão de tipos de dados, se necessário. 
- Salve o dataset limpo em um arquivo data_clean.csv. 
"""

# Importação das bibliotecas
from map_produto_categoria import produto_categoria
from faker import Faker
from datetime import date
import pandas as pd
import numpy as np
import random

faker = Faker('pt_BR') # Gera instância de um objeto faker configurado para o idioma Português - BR
num_registros = 100    # Define o número de registros a serem criados como 100

# Variáveis de controle para geração de datas no formato date
data_inicial = date(2023,1,1)   # Início: 01/01/2023 
data_final   = date(2023,12,31) # Fim...: 31/12/2023 

# Inicia lista de vendas
vendas = []

# Função utilizada para gerar um registro do dataframe
def gera_registro(idx):
    produto = random.choice(list(produto_categoria.keys()))
    vendas.append({
        'ID': idx,
        'Data': faker.date_between(start_date=data_inicial, end_date=data_final),
        'Produto': produto,
        'Categoria': produto_categoria[produto],
        'Quantidade': random.randint(1,100),
        'Preço': round(random.uniform(15, 250), 2)
    })

# Gera a quantidade de registros desejada a partir da variável 'num_registros'
for idx in range(0,num_registros):
    gera_registro(idx)

# Transforma os registros gerados em dataframe
df_vendas = pd.DataFrame(vendas, columns=['ID','Data','Produto','Categoria','Quantidade','Preço'])

# Antes de remover duplicados da coluna de produtos
# print(df_vendas.to_string(index=False))

print('\n-------------------------')
print('REMOVE DUPLICATAS - PRODUTOS\n')

# ===== TRATAMENTO E LIMPEZA DE DADOS ===== #

# -- REMOVE DUPLICATAS -- 
# Regra: Produto deve ser único (aparecer apenas uma vez)
# Faz a tratativa das duplicatas da coluna de produtos, mantendo a primeira aparição
df_vendas.drop_duplicates(subset=['Produto'], inplace=True, keep='first')



# Cria uma nova coluna realizando o cálculo do total de vendas (Quantidade x Preço)
# df_vendas['total_vendas'] = df_vendas['Quantidade'] * df_vendas['Preço']