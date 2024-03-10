"""
Módulo Colletions - Counter (Contador)

Collection -> High-performance Container Datatypes


Counter -> Recebe um interável como parâmetri e cria um objeto do tipo Collections Counter que é parecido com um dicionário, contendo como chave o elemento de lista passado como parâmetro e como valor a quantidade de ocorrências desse elemento.
"""

# Utilizando o Counter
# Exemplo 1
from collections import Counter

# Podemos utilizar qualquer iterável aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 2, 1, 3, 2, 1, 3, 3, 3, 2, 4, 3]

# Utilizando o Counter
res = Counter(lista)
print(res)
print(type(res))
# Counter({3: 9, 1: 5, 2: 5, 4: 1})
# Veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências


# Exemplo 2
print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3
texto = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

palavras = texto.split()
print(palavras)
res = Counter(palavras)
print(res)

print(res.most_common(5)) # 5 palavras com mais ocorrências no texto
