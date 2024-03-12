"""
Funções com retorno

# OBS: Funções python que retornam valores, devem retornar estes valores com a palavra resevada return
# OBS: Não precisamos necessariamento criar uma variável para receber o retorno de uma função. Podemos passar a execução de função para outras funções.
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

