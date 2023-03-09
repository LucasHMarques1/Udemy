// o this vai acessar o objeto pessoa e com isso ele consegue acessar o atributo saudacao
const pessoa = {
    saudacao: 'Bom dia!',
    falar() {
        console.log(this.saudacao)
    }
}

pessoa.falar()
const falar = pessoa.falar
falar() // conflito entre paradigmas: funcional e Orientação a Objetos, o this vai apontar para saudacao só que o this não vai ser mais PESSOA, e com isso dá undefined

const falarDePessoa = pessoa.falar.bind(pessoa) // basicamente passa o objeto resolvendo o this, que no caso é PESSOA
falarDePessoa()
