//Feito por Leandro Schalemberg

let titulo = document.querySelector("h1");
titulo.innerText = "Modificado por JavaScript";

let link = document.querySelector("a");
link.innerText = "Link modificado por JavaScript";

let lista = document.querySelector("ul");
lista.innerHTML = "<li>Item 1</li><li>Item 2</li><li>Item 3</li>";

let lista2 = document.querySelector("ol");
lista2.innerHTML =
  "<li><a href='https://prozeducacao.com.br'> Link 1</a></li><li><a href='https://prozeducacao.com.br'>Link 2</a></li><li><a href='https://prozeducacao.com.br'>Link 3</a></li>";
