# Teste e visualização das consultas SQL com pandasql

import os
import pandas as pd
from pandasql import sqldf

# Formatação do caminho do arquivo para outras máquinas
base_dir    = os.path.dirname(__file__)  
caminho_arq = os.path.join(base_dir, "..", "Parte 1", "data_clean.csv")
caminho_arq = os.path.normpath(caminho_arq)

# Carrega a tabela de vendas
vendas = pd.read_csv(caminho_arq)

""" 
Listar o nome do produto, categoria e a soma total de vendas (Quantidade * Preço) para cada produto. 
Ordene o resultado pelo valor total de vendas em ordem decrescente. 
"""

query = """
    SELECT
        Produto,
        Categoria,
        SUM(total_vendas) AS total_vendas
        FROM vendas
        GROUP BY Produto
        ORDER BY SUM(total_vendas) DESC
    """

primeira_consulta = sqldf(query)
print(primeira_consulta)
print('\n==========================================================\n')

""" 
Identificar os produtos que venderam menos no mês de junho de 2024.
"""

query = """
    SELECT
        Produto,
        SUM(total_vendas) AS total_vendas
        FROM vendas
        WHERE Data BETWEEN '2023-06-01' AND '2023-06-30'
        GROUP BY Produto
        ORDER BY total_vendas
    """

segunda_consulta = sqldf(query)
print(segunda_consulta)