"""
Estruturas condicionais
if, else, elif
"""

idade = 6

if idade < 18:
    print('Menor de idade')


idadePessoa = int(input("Qual sua idade? "))

if idadePessoa < 18:
    print("Menor de idade")
else:
    print("Maior de idade")


idade1 = int(input("Qual sua idade? "))

if idade1 < 16:
    print("Você é menor de idade")
elif idade1 == 18:
    print("Você tem 18 anos")
else:
    print("Você é maior de idade")
