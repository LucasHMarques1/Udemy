"""
Funções com retorno

# OBS: Funções python que retornam valores, devem retornar estes valores com a palavra resevada return
# OBS: Não precisamos necessariamento criar uma variável para receber o retorno de uma função. Podemos passar a execução de função para outras funções.
# OBS: SObre a palavra reservada return:
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;
"""

# Vamos refatorar esta função para que ela retorno o valor
def quadrado_de_7 ():
    return (7 * 7)

ret = quadrado_de_7()
print(f'Retorno {ret}')
# OU
print(quadrado_de_7())

# Refatorando a primeira função
def diz_oi():
    return "oi"
print(diz_oi())

# Exemplo 1
def diz_oi():
    return 'Oi'
    print('Teste')

print(diz_oi())

# Exemplo 2
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# Exemplo 3
def outra_funcao():
    return 2, 3, 4, 5

# num1, num2, num3, num4, num5 = outra_funcao()
# print(num1, num2, num3, num4, num5)
print(outra_funcao())

# Vamos criar uma função para jogar a moeda
from random import random
def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'
print(f'Lado da moeda sorteada foi {joga_moeda()}')

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária
def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    # else
       # return False
    return False
print(eh_impar())
