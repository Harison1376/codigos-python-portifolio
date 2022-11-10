"""
Mapas são conhecidos em Python com dicionários

Dicionários são representados por chaves {}


receita = {'jan': 100, 'fev': 120, 'mar': 300}
print('Abaixo impressão das chaves')
for chave in receita:  # para cada chave dentro de receita
    print(chave) # imprima a chave

print('Abaixo impressão dos valores das chaves')
for chave in receita:  # para cada chave dentro de receita
    print(receita[chave])  # imprima o valor da receita

print('Abaixo impressão melhorada')
for chave in receita:
    print(f'Em {chave}  Recebi R$: {receita[chave]} ')




# acessando as chaves
print(receita.keys())

print('Acesso aos valores das chaves')  # modo Pythonico
for chave in receita.keys():
    print(receita[chave])

# acessando o valores

print(receita.values())

for valor in receita.values():  # para valor em receita ,modo Pythonico de acesso a valores
    print(valor)  # imprima os valores

print(receita)

# Desempacotamento de dicionários

print(receita.items())
for chave, valor in receita.items():
    print(f'Chave => {chave} e Valor => {valor}')
"""

receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Soma, Valor Maximo*, Valor Minimo*, Tamanho  para valores inteiros e reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

print('Abaixo impressão das chaves')
for chave in receita:  # para cada chave dentro de receita
    print(chave)  # imprima a chave

print('Abaixo impressão dos valores das chaves')
for chave in receita:  # para cada chave dentro de receita
    print(receita[chave])  # imprima o valor da receita

print('Abaixo impressão melhorada')
for chave in receita:
    print(f'Em {chave} Recebi R$: {receita[chave]} ')
