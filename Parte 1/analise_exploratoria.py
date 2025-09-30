import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados do arquivo .csv
df_vendas = pd.read_csv('data_clean.csv')
df_vendas['Data'] = pd.to_datetime(df_vendas['Data'])

# === PRIMEIRA VISUALIZAÇÃO: GRÁFICO DE LINHA COM O TOTAL DE VENDAS POR MÊS === #

# Agrupa a soma do total de vendas por mês
vendas_mensais = df_vendas.resample('MS', on='Data')['total_vendas'].sum()

plt.style.use("bmh")
plt.figure(figsize=(14,7))
plt.plot(vendas_mensais.index, vendas_mensais.values, marker='o', color='green')
plt.title("Total de Vendas por Mês")
plt.xlabel("Mês")
plt.ylabel("Total de Vendas (R$)")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--')
plt.savefig('vendas_mes.png')
plt.show()

# === SEGUNDA VISUALIZAÇÃO: GRÁFICO DE BARRAS COM AS CATEGORIAS MAIS VENDIDAS === #

plt.style.use("bmh")
plt.figure(figsize=(14,7))
plt.barh(df_vendas['Categoria'], df_vendas['total_vendas'], color='green')
plt.title("Vendas por Categoria")
plt.xlabel("Total de Vendas (R$)")
plt.ylabel("Categoria")
plt.savefig('vendas_categoria.png')
plt.show()