"""
**kwargs

Poderiamos chamar este parâmetro de **xix, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs existe que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.
"""

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita da {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='azul', vanessa='banco')

# OBS: Os parâmetros *args e **kwars não são obrigatórios.
cores_favoritas()
cores_favoritas(geek='navy')

# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythânico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funções, podemos ter:
# - Parâmetro obrigatórios
# - *args
# - Parâmetros default (não obrigatórios)
# - **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 6, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entenda por quê é importante manter a ordem dos parâmetros na declaração

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return (a, b, args, instrutor, kwargs)

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
