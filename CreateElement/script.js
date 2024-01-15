let adicionaElemento = document.createElement("h1");
adicionaElemento.innerText = "Exercício - JavaScript DOM";
adicionaElemento.id = "titulo";

let produto = document.createElement("div");
produto.id = "produto";

let nomeProduto = document.createElement("h2");
nomeProduto.textContent = "Notebook Dell";
produto.appendChild(nomeProduto);

let imagemProduto = document.createElement("img");
imagemProduto.src = "NotebookDell.jpg";
imagemProduto.id = "imagem";
produto.appendChild(imagemProduto);

let descricaoProduto = document.createElement("p");
descricaoProduto.textContent =
  "Exelente notebook para trabalho e estudos, com processador i7 e 16GB de RAM";
produto.appendChild(descricaoProduto);

let precoProduto = document.createElement("p");
precoProduto.textContent = "Preço: R$ 4.500,00";
produto.appendChild(precoProduto);

let botaoComprar = document.createElement("button");
botaoComprar.textContent = "Comprar";
produto.appendChild(botaoComprar);

let elementoPai = document.querySelector("body");
elementoPai.appendChild(adicionaElemento);
elementoPai.appendChild(produto);
