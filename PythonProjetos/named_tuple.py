"""
Modulo Collections - Named Tuple
Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

Recape tuplas
tupla = (1, 2, 3)
print(tupla[1])

Name Tuple => É como se eu nomeasse a tupla ou seja mais ou menos assim tupla = (num1=1, num2=2, num3=3), ou seja são
tuplas diferenciadas onde especiicamos um nme para a mesma e também parâmetros

**********************************************************************************************************************

# FORMA 1 DE DECLARAÇÃO DE namedtuple
cachorro = namedtuple('cachorro', 'idade raca nome')  # a definição fica assim, variavel do tipo namedtuple, como
# O nome cachorro, e idade, raça e nome são parametros

# FORMA 2 DE DECLARAÇÃO DE namedtuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')  # Igual a forma 1 , porém separada por vigula

# FORMA 3 - DECLARAÇÃO DE namedtuple - PREFERIDA PELO PROFESSOR
cachorro = namedtuple('cachorro' ['idade', 'raca', 'nome'])  # fica mais clara par se entender
"""
# FAZENDO UM IMPORT

from collections import namedtuple
# precisamos então apos isso definir o nome e os parâmetros para essa tupla

# FORMA 2 DE DECLARAÇÃO DE namedtuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')  # Igual a forma 1 , porém separada por vigula

# USANDO - forma 2

ray = cachorro(idade=2, raca='chow-chow', nome='perninha')
print(ray)

# acessando os dados
# forma 1

print(ray[0])  # idade
print(ray[1])  # raca
print(ray[2])  # nome

# forma 2

print(ray.idade)  # idade
print(ray.raca)  # raça
print(ray.nome)  # nome


# Posso ainda usar
print(ray.index('chow-chow'))
print(ray.count('chow-chow'))
