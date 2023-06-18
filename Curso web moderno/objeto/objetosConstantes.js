// pessoa -> 123 -> {...}
const pessoa = { nome: 'Joao'}
pessoa.nome = 'Pedro'
console.log(pessoa)

// pessoa -> 456 -> {...}
// pessoa = { nome: 'Ana' }

Object.freeze(pessoa)

pessoa.nome = 'Maria'
pessoa.end = 'Rua ABC'
delete pessoa.nome

console.log(pessoa.nome) // Pedro
console.log(pessoa) // { nome: 'Pedro' }

const pessoaConstante = Object.freeze({ nome: 'Joao' })
console.log(pessoaConstante)
