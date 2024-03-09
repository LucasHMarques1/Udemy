"""
Listas

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICAS e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, se você criar um array de tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
    - Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
    - Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representadas por colchetes: []
"""

# Exemplo de listas
type([])

lista1 = [1, 99, 4, 27, 15, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista
num = int(input('Digite um número: '))
if num in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número 8')



letra = input('Digite um número: ')
if letra in lista5:
    print(f'Encontrei a letra {letra}')
else:
    print(f'Não encontrei a letra {letra}')


# Podemos facilmente ordenar uma lista
lista1.sort() # Ordenar a lista (ordem numérica crescente)
print(lista1)

lista5.sort() # Ordenar a lista (ordem alfabética crescente)
print(lista5)


# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1)) # Contando quantos "1" tem na lista
print(lista5.count('e')) # Contando quantos "e" tem na lista


# Adicionar elementos em listas
"""
Para adicionar elementos em listas, utilizamos a função append
obs: com append, só é possível adicionar um elemento por vez
"""
print(lista1)
lista1.append(42) # Adiciona o número 42 ao final da lista
print(lista1)

lista1.append([8, 3, 1]) # Adiciona a lista [8, 3, 1] ao final da lista
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

if [22, 27, 27] in lista1: # Dá inválido, pois só é possível ver 1 item da lista
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')
   

lista1.extend([123, 44, 67]) # Adiciona cada elemento da lista ao final da lista
print(lista1)

lista1.extend('Geek') # Adiciona cada letra da string ao final da lista
print(lista1)



# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo Valor') # Adiciona o valor 'Novo Valor' na posição 2
print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

lista1.extend(lista2)
print(lista1) # mesma coisa, misturar listas

# Forma 1
lista1.reverse() # Inverte a lista
lista2.reverse() # Inverte a lista
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1]) # Inverte a lista
print(lista2[::-1]) # Inverte a lista

# Copiar uma lista
lista6 = lista2.copy()

print(len(lista5)) # Tamanho da lista
print(lista5)

# Podemos remover facilmente o último elemento de uma lista
print(lista5)
lista5.pop() # Remove o último elemento da lista e retorna o elemento que foi removido
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita deste índice serão deslocados para a esquerda.
lista5.pop(2) # Remove o elemento de índice 2
# OBS: Se não houver elemento no índice informado, teremos o erro IndexError

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear() # Limpa a lista

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3 # Repete a lista 3 vezes

# Podemos facilmente converter uma string para uma lista
# Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split() # Por padrão, o split separa os elementos da lista pelo espaço entre elas
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = "Programação,em,python, essencial"
print(curso)
curso = curso.split(',')
print(curso)

lista7 = ['Programação', 'em', 'python', 'essencial']
print(lista7)

# Abaixo estamos falando: Pega a lista7, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista7)
print(lista7)

# Abaixo estamos falando: Pega a lista7, coloca um $ entre cada elemento e transforma em uma string
curso = '$'.join(lista7)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive ,misturando esses dados
lista8 = [1, 2, 34, True, 'Geek', 'd', [1, 2, 3], 430434503438]
print(lista8)
print(type(lista8))

# Iterando sobre listas
# Exemplo 1
for elemento in lista1:
    print(elemento)

# Exemplo 2 - Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Gerar indice em um for
cores = ['verde', 'amarelo', 'azul', 'branco']
for indice, cor in enumerate(cores):
    print(indice, cor)


# Encontrar o indice de um elemento na lista
numeros = [5, 6, 6, 3, 7]

# Em qual índice da lista está o valor 4?
print(numeros.index(4)) # Retorna o índice do primeiro elemento encontrado
# print(numeros.index(19)) # Gera ValueError

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1)) # Buscando apartir do indice 1

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(3, 1, 4)) # Buscar o índice do valor 3, entre os índices 1 a 4

# Revisão de slicing

# lista(inicio:fim:passo)
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro 'inicio'
listaN = [1, 2, 3, 4]
print(listaN[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice da lista com o parâmetro 'fim'
print(listaN[:4]) # Começa do 0, pega até o índice 4 - 1
print(listaN[1:4]) # Começa do 1, pega até o índice de 4 - 1

# Trabalhando com slice de lista com o parâmetro 'passo'
print(listaN[1::2]) # Começa em 1, vai até o final, de 2 em 2

# Invertendo valores em uma lista
print(listaN[0::-1]) # Começa  em 0, vai ao inverso
listaN.reverse()
print(listaN)

# Soma+, Valor Máximo+, Valor Mínimo+, Tamanho
# * Se os valores forem todos inteiros ou reais.
listaA = [1, 2, 3, 4, 5, 6]
print(sum(listaA)) # soma
print(max(listaA)) # máximo valor
print(min(listaA)) # minimo valor
print(len(listaA)) # tamanho da lista

# Transformando uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
lista = [1, 2, 4]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
# OBS: Se tivermos mais elementos para desempacotar do que variáveis para receber os valores, teremos ValueError

# Copiando uma lista para outra(Shallow Copy e Deep Copy)
# Forma 1
lista = [1, 2, 3]
print(lista)
nova = lista.copy() # cópia
print(nova)
nova.append(4)
print(lista)
print(nova)
# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python é chamado de Deep Copy(cópia profunda)

# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)
nova = lista # cópia
print(nova)
nova.append(4)
print(lista)
print(nova)
# Veja que utiizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas após realiar modificação em uma das listas, essa modificação se refletiu em ambas as listas. Isso em Python é chamado de Shallow Copy

