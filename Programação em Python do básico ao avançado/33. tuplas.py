"""
Tuplas(tuple)

Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são inutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla.
"""

# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento
tupla3 = (4) # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla!
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))
# Conclusão: Podemos concluir que tuplas são definidas pela virgula e não pelos parenteses

# Podemos gerar tupla dinamica com range(inicio:fim:passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python')
escola, curso = tupla
print(escola)
print(curso)
# OBS: Gera erro (ValueError) se colocarmos um numero diferente para desempacotar

# Metodos para: adição e remoção de elementos nas tuplas não existem, dados os fatis que elas são imutáveis
# Soma+, Valor Maximo, Valor Minimo+ e Tamanho
# Se os valores forem inteiros ou reais
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla)) # soma
print(max(tupla)) # maximo valor
print(min(tupla)) # minimo valor
print(len(tupla)) # tamanho

# Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6)
print(tupla2)
print(tupla1 + tupla2) # Resultado = (1, 2, 3, 4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)
# OU
tupla1 = tupla1 + tupla2 # Tuplas são imutaveis, mas podemos alterar seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'c', 'a', 'e', 'f')
print(tupla.count('c')) # Quantos C tem na tupla

escola = tuple('Geek University') # String para tupla
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas
# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados de uma coleção
# Exemplo1
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses)

# Acesso a elementos de uma tupla também é semelhante de uma lista
print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i += i

# Verificando qual indice de um elemento está na tupla
print(meses.index('Playstation'))
# OBS: Caso o elemento não exista, srá gerado ValueError

# Slicing
# tupla(inicio:fim:passo)
print(meses[0:]) # todos
print(meses[5:9]) # Vai retornar de Maio até Setembro

# Por quê utilizar tuplas?
# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro - Isso porque trabalhar com elementos imutaveis traz segurança para o código.

# Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)
nova = tupla # Na tupla não temos o problema Shallow Copy
print(nova)
print(tupla)

outra =(4, 5, 6)
nova += outra
print(nova)
print(tupla)
