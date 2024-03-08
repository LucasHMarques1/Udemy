"""
Loop While

while expressão_booleana:
       // execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeira ou falsa

"""
# Exemplo 1
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.
# DO WHILE não existe no python

# Exemplo 2
resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')
