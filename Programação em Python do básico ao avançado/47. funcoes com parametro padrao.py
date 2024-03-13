"""
Funções com parâmetro padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional
# Exemplo de função onde a passagem de parâmetro seja opcional

"""
print('Geek University')
print()

def exponencial(numero, potencia=2): # potencia=2 é o parâmetro padrão acaso não receber valor
    return numero ** potencia

print(exponencial(2, 3)) # 2 * 2 * 2 = 8
# print(exponencial()) # typeError
print(exponencial(3, 2)) # 3 * 3 = 9

# OBS
# Se o usuário passar somente 1 argumento, este será atribuído ao parâmetro número, e será calculado o quadrado desse número
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro número e o segundo ao parâmetro potência. Então será calculado essa potência.

def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(5, 3)) # 5 * 5 * 5 = 125
print(exponencial(3)) # 3 * 2 = 9
print(exponencial()) # 4 ** 2 = 16


# OBS: Em funções Python, os parâmetros com valores default (padrão) devem sempre estar ao final da declaração.
# def soma(num2=2, num1):
#     return num1 + num2
# print(soma(4, 3))
# print(soma(4)) # TypeError, o primeiro parâmetro num2 vai receber 2
# print(soma()) # TypeError

# Exemplo mais complexo
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Angelina'))
print(mostra_informacao(nome='Angelina'))

# Por quê utilizar parâmetros com valor default?
# - Nos permite ser mais flexíveis nas funções
# - Evita erros com parâmetros incorretos
# - Nos permite trabalhar com exemplos mais legíveis de código

# Quais tipos de dados podemos utilizar como valores default para parâmetros?
# - Qualquer tipo de dado:
    # - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc.

def mat(num1, num2, fn=soma):
    return fn(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))


# Escopo - Evitar problemas e confusões...

# Variaveis globais
# Variaveis locais

instrutor = 'Geek' # Variável global

def diz_oi():
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor}'
print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
    prof = 'Geek' # Variável local
    return f'Olá {prof}'
print(diz_oi())
# print(prof) # NameError

# Atenção com variáveis globais (Se puder evitar, evite!)
total = 0

def incrementa():
    global total # Avisamos que queremos utilizar a variável global

    total = total + 1 # UnboundLocalError
    return total

print(incrementa())


# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável
def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

# print(dentro()) # NameError
