/* 
=================== PRIMEIRA CONSULTA ==================
- Listar o nome do produto, categoria e a soma total de vendas (Quantidade * Preço) para cada produto. 
- Ordenar o resultado pelo valor total de vendas em ordem decrescente. 
*/

/* 
Essa consulta seleciona as colunas Produto e Categoria e calcula a soma de total_vendas para cada produto dentro de sua categoria. 
O resultado é agrupado por Produto e Categoria e ordenado do maior para o menor total de vendas.
*/
SELECT
    Produto,
    Categoria,
    SUM(total_vendas) AS total_vendas
    FROM vendas
    GROUP BY Produto, Categoria
    ORDER BY total_vendas DESC

/* ========================== SEGUNDA CONSULTA ========================= */ 
/* - Identificar os produtos que venderam menos no mês de junho de 2023. */

/* 
Para esta consulta, foi realizada a seleção da coluna de Produto juntamente a soma
da coluna do total de vendas, tendo como resultado a soma total das vendas do produto.
Também foi aplicado o filtro "WHERE Data BETWEEN '2023-06-01' AND '2023-06-30'" para que fossem 
consultadas apenas as vendas do mês de Junho, utilizando BETWEEN para melhor desempenho.
Por fim, O resultado é agrupado por Produto e ordenado de forma crescente pelo 
total de vendas, mostrando primeiro os produtos menos vendidos.
*/
SELECT
    Produto,
    SUM(total_vendas) AS total_vendas
    FROM vendas
    WHERE Data BETWEEN '2023-06-01' AND '2023-06-30'
    GROUP BY Produto
    ORDER BY total_vendas