"""
modulo Collections : Ordered dict
https://docs.python.org/3/library/collections.html#collections.OrderedDict

# em um dicionario, a ordem de isnerção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')

# fazendo um import
from collections import OrderedDict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')


"""
from collections import OrderedDict

# Entendo a diferenço entre Dict e Ordered Dict

# Dicionarios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # resposta desse print é True, pois nese caso o dicionario nao olha para a ordem


# OrderedDict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # nesse caso como estamos usando o Ordered Dict então vai haver diferença

