"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string'''

"""
# - Estiver entre àspas duplas triplas -> """uma string"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = '''Angelina
Jolie'''
print(nome)
print(type(nome))

nome = 'Lucas'
print(nome.upper()) # maiuscula
print(nome.lower()) # minuscula
print(nome.split()) # lista -> ['L', 'u', 'c', 'a', 's']
print(nome)

