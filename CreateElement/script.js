let adicionaElemento = document.createElement("h1");
adicionaElemento.innerText = "Exercício - JavaScript DOM";
adicionaElemento.id = "titulo";

//método complexo
let produto = document.createElement("div");
produto.innerHTML = `<h2>Notebook Dell</h2>
<img src="NotebookDell.jpg" id="imagem" />
<p>Exelente notebook para trabalho e estudos, com processador i7 e 16GB de RAM</p>`;

//método simples
let precoProduto = document.createElement("p");
precoProduto.textContent = "Preço: R$ 4.500,00";
produto.appendChild(precoProduto);

let botaoComprar = document.createElement("button");
botaoComprar.textContent = "Comprar";
produto.appendChild(botaoComprar);

let elementoPai = document.querySelector("body");
elementoPai.appendChild(adicionaElemento);
elementoPai.appendChild(produto);
