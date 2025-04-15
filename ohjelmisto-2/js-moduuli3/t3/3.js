'use strict';
const names = ['John', 'Paul', 'Jones'];

let lista = '';
for (let name of names) {
  lista += `<li>${name}</li>`
}

document.querySelector('#target').innerHTML=lista;
