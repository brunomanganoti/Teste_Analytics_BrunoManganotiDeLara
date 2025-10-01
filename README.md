<a id="inicio-readme"></a>

<!-- INÍCIO -->
<div style="justify-content: right; display: flex;">
      <img src="img/analytics2.gif" alt="analytics" width="110px" height="70px">
</div>

<!-- SOBRE O PROJETO -->
# 📊 Projeto - Teste Analytics
* Este repositório contém um estudo fictício de geração, limpeza e análise de dados de vendas, com foco em simular cenários reais para prática de Data Analytics.
* O projeto permite tanto utilizar o dataset original (já incluído no repositório) quanto gerar novos dados aleatórios para diferentes análises.

<p align="right">(<a href="#inicio-readme">voltar ao início</a>)</p>

# 🛠️ Tecnologias utilizadas
   * Python 3.10+
   * Pandas -> manipulação de dados
   * Matplotlib -> visualização
   * Faker -> geração de dados fictícios
   * SQL -> consultas e análises

<p align="right">(<a href="#inicio-readme">voltar ao início</a>)</p>

# 📂 Estrutura do Repositório
   ```bash
📂 Teste_Analytics_BrunoManganotiDeLara
│
├── 📁 Parte 1 # Geração dos dados e limpeza
│   │
│   ├── 📁 Gráficos # Visualizações geradas
│   │   │
│   │   ├── vendas_categoria.png
│   │   │
│   │   └── vendas_mes.png
│   │
│   ├── analise_exploratoria.py
│   │
│   ├── data_clean.csv
│   │          
│   ├── geracao_limpeza_dados.py
│   │
│   └── map_produto_cat_preco.py
│   
├── 📁 Parte 2 # Consultas SQL
│   │
│   ├── consultas_sql.sql
│   │
│   └── teste_consulta.py
│
├── 📁 Parte 3 # Relatório de Insights
│   │
│   └── relatorio_insights.md
│
├── 📘 README.md                   
│
└── 📦 requisitos.txt # Dependências do projeto
   ```

<p align="right">(<a href="#inicio-readme">voltar ao início</a>)</p>

# ⚙️ Instruções
Siga as etapas abaixo para o funcionamento correto dos scripts.

### 1️⃣ Clone o repositório
   ```bash
   git clone https://github.com/brunomanganoti/Teste_Analytics_BrunoManganotiDeLara.git

   cd Teste_Analytics_BrunoManganotiDeLara
   ```
### 2️⃣ Instale as dependências do projeto
   ```bash
   pip install -r requisitos.txt
   ```

<p align="right">(<a href="#inicio-readme">voltar ao início</a>)</p>


# ▶️ Como funciona
Etapas para geração das visualizações e novas análises

### ℹ️ Observações iniciais
* As análises originais foram feitas a partir dos dados encontrados no arquivo 'data_clean.csv' originais do repositório.
* Caso queira gerar novos dados e gráficos para diferentes análises, siga as etapas abaixo.

### 1️⃣ Geração e limpeza dos dados
Execute o script para criar um dataset fictício e aplicar limpeza básica de dados (remoção de duplicatas e tratamento de nulos):
```bash
cd "Parte 1" # se necessário
py geracao_limpeza_dados.py
```
Isso vai gerar o arquivo 📄 <mark>data_clean.csv</mark>.

### 2️⃣ Análise exploratória
Para executar a análise exploratória e gerar novos gráficos:
```bash
cd "Parte 1" # se necessário
py analise_exploratoria.py
```
Serão criados os arquivos:
* 📊 <mark>vendas_categoria.png</mark> -> gráfico de vendas por categoria
* 📊 <mark>vendas_mes.png</mark> -> gráfico de vendas por mês

### 3️⃣ Consultas SQL
O arquivo ⛃ <mark>consultas_sql.sql</mark> na pasta 'Parte 2' contém exemplos de consultas SQL para visualização dos dados.



<p align="right">(<a href="#inicio-readme">voltar ao início</a>)</p>