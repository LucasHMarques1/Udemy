"""
Definindo Funções

- Funções são pequenas partes do código que realizam tarefas espedíficas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela é bom fazer uma verificação para que a função seja simplificada.

Exemplos de funções:
- print()
- len()
- max()
- min()
- count()
- e muitas outras...
"""
# Exemplo de utilização de funções:
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()
print(cores)

cores.append('roxo')
print(cores)

cores.clear()
print(cores)

# print(help(print))
# DRY - Dont`t Repeat Yourself - Não repita você mesmo / Não repita seu código

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é: 

def nome_da_funcao(parametros_de_entrada):
    bloco_de_funcoes
    

Onde:
nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por underline (Snake Case):
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da funcao ou implementação, é onde o processamento da função acontece.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo uma função. Também abbrimos o bloco de código com o já conhecido dois pontos : que é utilizado em Python para definir blocos.
"""

# Definindo a primeira função
def diz_oi():
    print('oi!')
"""
OBS:
1 - Veja que, dentro das funções podemos utilizar outras funções:
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;7
4 - Veja que está função não retorna nada;
"""

# Utilizando funções

# Chamada de execução
diz_oi()

"""
ATENÇÃO

Nunca esqueça de utilizar o parênteses ao executar uma função

Errado!
diz_oi

Certo!
diz_oi()

Errado!
diz oi()
"""

# Exemplo 2
def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

cantar_parabens()
cantar_parabens()
cantar_parabens()
cantar_parabens()
# OU (Muito melhor)
for n in range(5):
    print(n)
    cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar está função através da variável
canta = cantar_parabens
canta()
