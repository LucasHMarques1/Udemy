"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a Teoria dos COnjuntos da Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados:
- Sets (conjuntos) não possuem valores ordenados:
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles, Quando não precisamos se preocupar com chaves, valores e items duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (SET) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;
"""

# Definindo um conjunto:
# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 7, 2, 3, 8}) # Repare que temos valores repetidos
print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error e não terá parte do conjunto.

# Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Assim como todo outro conjunto Python, podemos colocar tipos de dados misturados em Sets
