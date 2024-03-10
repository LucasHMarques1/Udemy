"""
Módulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar uma lambda para isso. Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não existe, essa chave ser[a criada e o valor default será atribuído.

OBS: Lambda são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.
"""

dicionario = {'curso': 'Programação em Python'}
print(dicionario)
print(dicionario['curso'])
# print(dicionario['outro']) # KeyError
print(type(dicionario))

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)
dicionario['curso'] = 'Programação em Python'
print(dicionario)
print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não.
print(dicionario)
