"""
Mapas -> Conhecidos em Python como DIcionários

Dicionários em Python são representados por chaves {}
"""

receita = {'jan':100, 'fev':200, 'mar':400}

# Iterar sobre dicionários
for chave in receita: # Imprimindo chaves
    print(chave)

for chave in receita: # Imprimindo valores
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

# Acessando as chaves
print(receita.keys()) # Dicionário de chaves

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma+, Valor Máximo, Valor Minímo+, Tamanho
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
