CREATE PROCEDURE RelatorioDiarioVendas
AS
BEGIN
    SELECT DataVenda, ProdutoID, SUM(Quantidade) as QuantidadeTotal
    FROM Vendas
    GROUP BY DataVenda, ProdutoID
    ORDER BY DataVenda DESC;
END