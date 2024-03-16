CREATE FUNCTION ContarClientesDiarios(@Data DATE)
RETURNS INT
AS
BEGIN
    DECLARE @Quantidade INT;

    SELECT @Quantidade = COUNT(*)
    FROM Clientes
    WHERE DataCadastro = @Data;

    RETURN @Quantidade;
END;

SELECT dbo.ContarClientesDiarios('2024-03-16');
