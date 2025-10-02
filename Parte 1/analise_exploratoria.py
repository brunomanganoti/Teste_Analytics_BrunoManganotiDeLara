import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados do arquivo .csv
df_vendas = pd.read_csv('data_clean.csv')
df_vendas['Data'] = pd.to_datetime(df_vendas['Data'])

print('\n-------------------------------')
print('APÓS CÁLCULO DO TOTAL DE VENDAS\n')
print(df_vendas.to_string(index=False)) 

# === PRIMEIRA VISUALIZAÇÃO: GRÁFICO DE LINHA COM O TOTAL DE VENDAS POR MÊS === #
# Agrupa a soma do total de vendas por mês
vendas_mensais = df_vendas.resample('MS', on='Data')['total_vendas'].sum()

plt.style.use('classic')
plt.figure(figsize=(12,8))
plt.plot(vendas_mensais.index, vendas_mensais.values, marker='o', color='green')
plt.title("Total de Vendas por Mês")
plt.xlabel("Mês", fontsize=15)
plt.ylabel("Total de Vendas (R$)", fontsize=15)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--')
plt.tight_layout()
plt.savefig('Gráficos/vendas_mes.png')

# === SEGUNDA VISUALIZAÇÃO: GRÁFICO DE BARRAS HORIZONTAIS COM AS CATEGORIAS MAIS VENDIDAS === #
vendas_categoria = df_vendas.groupby('Categoria')['total_vendas'].sum().reset_index()
cores = ['blue','red','orange','skyblue','yellow','magenta','green','pink','cyan']

plt.style.use('classic')
plt.figure(figsize=(12,8))
plt.barh(vendas_categoria['Categoria'], vendas_categoria['total_vendas'], color=cores)

plt.title("Vendas por Categoria")
plt.xlabel("Total de Vendas (R$)", fontsize=15)
plt.ylabel("Categoria", fontsize=15)
plt.grid(True, linestyle='--')
plt.tight_layout()
plt.savefig('Gráficos/vendas_categoria.png')

print(
'''
-----------------
Gráficos gerados!
-----------------
Local: ../Parte 1/Gráficos/
''')

# Obs: As observações e insights estão no relatório da Parte 3!