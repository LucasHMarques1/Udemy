"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java
for(int i = 0; i < 10; i++){
    // execução do loop
}

Python
for item in interavel:
    // execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores interáveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'

- Lista
    lista = [1, 3, 5, 7, 9]

- Range
    numeros = range(1, 10)

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
     print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
     print(numero)

# Exemplo de for 3 (Iterando sobre um range)
# OBS: range(valor_inicial, valor_final) - O número 10 não pega, por ser o último
for numero in range(1, 10):
     print(numero)




for indice, letra in enumerate(nome): # Exemplo: ((0, 'L'), (1, 'u'), (2, 'c'), (3, 'a'), (4, 's'))
     print(nome[indice])



qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1);
     num = int(input(f'Informe o {n} / {qtd} valor: '))
     soma = soma + num
print(f'A soma é {soma}')
