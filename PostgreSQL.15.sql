CREATE DATABASE MeuBancoDeDados;
USE MeuBancoDeDados;

CREATE TABLE Clientes (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Pedidos (
    PedidoID INT PRIMARY KEY,
    ClienteID INT,
    Produto VARCHAR(100),
    Quantidade INT,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
);

CREATE TRIGGER NovoPedido
AFTER INSERT
ON Pedidos
FOR EACH ROW
BEGIN
    DECLARE @ClienteID INT;
    DECLARE @Produto VARCHAR(100);
    SET @ClienteID = NEW.ClienteID;
    SET @Produto = NEW.Produto;
END;
