function Pessoa() {
    this.idade = 0

    const self = this // acessar o THIS que no caso é de PESSOA.
    setInterval(function() {
        self.idade++
        console.log(self.idade)
    }/* .bind(this) */ , 1000) //dispara outra função apartir de um intervalo que eu escolhi
}

new Pessoa
