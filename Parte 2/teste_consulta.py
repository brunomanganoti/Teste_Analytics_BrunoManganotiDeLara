import os
import pandas as pd
from pandasql import sqldf

# Caminho do arquivo
# Formatação do caminho para outras máquinas
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