"""

Dicionarios:
OBS: em algumas linguagens de programação os dicionarios python, são conhecidos por mapas

Dicionários são coleções de tipo chave/valor
Dicionários são representados por chaves  {}

print(type({}))

OBS: Sobre Dicionários
    - chave e valor são separados por dois pontos 'chave:valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados

# Criação de dicionários

# Forma 1 (mais comum para criação de dicionários)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br='Brasil', Eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos
# forma 1 - Acessando via chave, damesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# Caso tentemos fazer acesso a uma chave que não existe teremos o erro KeyError

# Forma2 - Acesando dado via get - RECOMENDADA
print(paises.get('br'))
print(paises.get('ru'))

# CASO O GET NAO ENCONTRE O OBJETO COM A CHAVE IFORMADA SERA RETORNADA O VALOR NONE E NÃO SERÁ GERADO KeyError

# FORMA 1 DE SE PROCURAR O PAIS
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises.get('ru')

if pais:
    print(f'Encontrei o pais {pais}')
else:
    print(f'Não encotrei')

# PODEMSO DEFINIR UM VALOR PADRÃO PARA CASO NAO ENCONTREMOS O OSBJETO COM A CHAVE INFORMADA
# FORMA 2 DE SE FAZER A BUSCA
pais = paises.get('PY', 'não encontrado')  # eu quero o pais com a chave ru, se nao encontar devolva nao encontrado
print(f'Encontrei o pais {pais}')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai','ru': "russia"}

# PODEMOS TAMBEM LOCALIZAR ITEM ESTA DENTRO DO DICIONÁRIO
print('br' in paises)  # esta chave esta dentro do dicionario paises
print('ru' in paises)
print('Estados Unidos ' in paises)  # neste caso aqui nao temos uma chave e sim um valor

if 'ru' in paises:
    russia = paises['ru']

# PODEMOS UTILIZAR QUALQUER TIPODE DADO (INT, FLOAT, STRING, BOOLEAN, INCLUSIE LISTA, TUPLAS DICIONARIOS, COMO CHAVES
# DICIONARIOS
# Tuplas por exemplo  sao bstante interessantes de serem utilizadas como chave de dicionarios por serem imutaveis
localidades = {  # AQUI ESTOU ABRINDO O MEU DICIONARIO
    (35.6895, 39.6917): 'Escritorio em Tókio',
    (40.7128, 74.0060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Pualo',
}  # AQUI ESTOU FECHANDOO DICIONARIO.

print(localidades)
print(type(localidades))

# ADICIONANDO ELEMENTOS DENTRO DOS DICIONARIOS

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# FOMRA 1 DE SE ADD  ELEMENTOS
receita['abr'] = 350
print(receita)

# FORMA 2

novo_dado = {'mai': 500}
receita.update(novo_dado)  # o mesmo que: ===>>> receita.update({'mai': 500}) <<<===

print(receita)

# ATUALIZANDO DADOS EM UM DICIONARIO
# FORMA 1
receita['mai'] = 550  # dessa forma estamos mais acrescendo do que atualizando

print(receita)

# FORMA 2
receita.update({'ma i': 600})  # nesta forma sim estamos atualizando
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizador dados em um dicionario é a mesma
# CONCLUSÃO 2: Em dicionários NÃO PODEMOS TER CHAVES REPETIDAS.

# REMOVENDO DADOS DE UM DICIONARIO
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
# FOMRA 1 -  mais comum pois dessa maneira podemos saber o que foi deletado pois retorna valor
ret = receita.pop('mar')
print(ret)
print(receita)
# OBS 1 aqui precisamos sempre informar  a chave, e se não encontrar retorna KeyError
# OBS 2 Ao remover um objeto, valor deste objeto é sempre retornado

# FORMA 2
del receita['fev']  # do dicionario receita,remova o mes de fevereiro
print(receita)
# OBS caso nao exista a chave ser removida, retorna KeyError, não retorna valor


"""
# Imagine um comercio eletronico, onde temos um carrinho de compras no qual add produtos.
""""
Carrinho de compras
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
        

# 1 - Poderiamos usar uma lista? sim.
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God Of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Teriamos que saber qual é o indide de cada informação no produto

# - Poderiamos utulizar uma tupla para isso? sim
carrinho = []
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God Of War 4', 1, 150.00)
carrinho = (produto1, produto2)

print(carrinho)

# Teriamos que saber qual é o indide de cada informação no produto

# 3 - Poderiamos utilizar um dicionario para isso? Sim
carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': "God of War", 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Nessa forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza sobre
# cada informação


# Métodos de dicionários.
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário (zerar dados)
d.clear()
print(d)

# Copiando um dicionário para outro
# forma 1 Deep copy
novo = d.copy()  # fazendo uma copia do dicionario dentro da variavel novo 
print(novo)  # imprimindo a nova variavel com o dicionário novodeep copy

novo['d'] = 4  # inserindo dentro do dicionário novo mais um valor

print(d)  # imprimindo o dicionário ogirinal
print(novo)  # imprima para mim o novo dicionario com o novo valor dentro
print(type(novo)

# fora 2 shallow copy

novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)

"""

# Forma nao usual de criação de dicionário
outro = {}.fromkeys('a',  'b')  # chave e valor
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido') # dentro do colchetes chave, fora valor
print(usuario)
print(type(usuario))

# OBS:  ) método fromkeys recebe dois parametros: um iteravel e um valor
# Ele vai gerara para cada valor do iteravael uma chave e irá atribuir a esta uma chave o valor informado

veja = {}.fromkeys('teste', 'valor')  # aqui ele criou para as letras T, E, S   'valor', nao repete em dicionario
print(veja)

# veja1 = {}.fromkeys(range(1, 11), 'novo')
# print(veja1)
