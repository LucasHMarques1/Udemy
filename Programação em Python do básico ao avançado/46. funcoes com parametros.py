"""
Funções com parâmetros(de entrada)

FUnções que recebem dados para serem processados dentro da mesma.
"""
# Refatorando uma função
def quadrado(numero):
    #return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(5))
print(quadrado(3))
# print(quadrado()) -> TypeError - Erro porque precisa de parâmetro


def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!') 

cantar_parabens('Fernanda')
cantar_parabens('Pedro')

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplo
def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(2, 10))
print(multiplica(8, 7))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se informarmos um número errado de parâmetros ou argumentos, teremos TypeError
# print(soma(2, 3, 4)) # TypeError - Passando argumentos a mais
# print(soma(2)) # TypeError - Passando argumentos a menos

# Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

# A diferença entre parâmetros e argumentos
# Parâmetros são variáveis declaradas na definição de uma função.
# Argumentos são dados passados durante a execução de uma função.

# A ordem dos parâmetros importa!
nome = 'Felicity'
sobrenome = 'Jones'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.
print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(sobrenome='Jolie', nome='Angelina'))
print(nome_completo(sobrenome=sobrenome, nome=nome))

# Erro comum na utilização do return
def soma_impares(numeros):
    total = 0
    for numero in numeros:
        if numero % 2 != 0:
            total += numero
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))
