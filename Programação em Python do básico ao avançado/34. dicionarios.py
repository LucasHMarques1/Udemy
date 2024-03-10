"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chave {}.

print(type({})

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave.valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;
"""
# Criação de dicionários

# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma de  lista/tupla
print(paises['br']) # Imprimir valor atráves da chave
# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada
print(paises.get('br'))
print(paises.get('ar')) # Resposta = None
pais = paises.get('ar')

# Podemos definir um valor padrão para caso não encontramos o objeto com a chave informada
# pais = paises.get('teste', 'Não encontrado')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises) # True
print('ru' in paises) # False

if 'uk' in paises:
    reinoUnido = paises['uk']

# Podemos usar qualquer tipo de dado(int, float, string, boolean, lista, tupla, dicionário, como chaves de dicionarios.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.4964): 'Escritório em Nova York',
    (38.5332, 29.5433): 'Escritório em Sâo Paulo',
}
print(localidades)
print(type(localidades))

receita = {'jan':100, 'fev':200, 'mar':300}
# Adicionar elementos em um dicionário
receita['abr'] = 350 # Mais usado
print(receita)
# OU
novo_dado = {'mai': 500} # receita.update({'dec':1000})
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário
# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update(['mai', 600])
print(receita)

# Conclusão 1 - A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# Conclusão 2 - Em dicionários. NÃO podemos ter chaves repetoidas.

# Remover dados de um dicionário
receita = {'jan':100, 'fev':200, 'mar':300}
# Forma 1
receita.pop('mar')
print(receita)
# OBS: Aqui precisamos SEMPRE informar a chave, a caso não encontre um elemento, um KeyError é retornado
# OBS: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2
del receita['fev']
print(receita)
# OBS: Se a chave não existir, será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de comprar na qual adicionamos produtos.
# Métodos de dicionários
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))
d.clear() # Limpar dicionario - Zerar dados
print(d)

# Copiando um dicionário para outro
# Forma 1
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

# Forma 2 - Shallow Copy
novo = d
print(novo)
novo['d'] = 4
print(novo)

# Forma não usual de criação de dicionários
outro = {}.fromkeys(('a', 'valor'))
print(outro)
print(type(outro))
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], ['desconhecido'])
print(usuario)
print(type(usuario))
# OBS: o método fromkeys recebe dois parâmetro: um interavel e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys((range(1, 11), 'novo'))
print(veja)
