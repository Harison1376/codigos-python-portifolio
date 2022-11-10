""""
Modulo Collections - Deque
https://docs.python.org/3/library/collections.html#collections.deque
Podemos deizer que Deque é uma lista de alta performance

"""

# import
from collections import deque

# Ciando deques

deq = deque('harison')  # vai transformar tudo que esta dentro do parenteses em  uma lista, mais facil de lidar
print(deq)

#  Adicionando elementos no deque
deq.append('CH')  # adiciona no final
print(deq)

# Adicinando no começo da lista
deq.appendleft('D')
print(deq)

# Removendo elementos
print(deq.pop())  # como em listas, remove o item do final e retorno o removido
print(deq.popleft())  # Remove o primeiro item da lista ou seja a esquerda da lista

print(deq)


