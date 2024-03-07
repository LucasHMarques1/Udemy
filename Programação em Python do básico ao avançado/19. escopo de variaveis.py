"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
- Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa

2 - Variaveis locais:
- Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java
int numero = 42;
"""

numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10
    print(novo)

print(novo) # Vai ser criada apenas se ativar o IF, por ser uma variável LOCAL
