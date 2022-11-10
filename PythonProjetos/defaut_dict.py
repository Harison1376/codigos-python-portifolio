""""
Modulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

RECAPE DICIONARIO
dicionario = {'curso': 'Programação em Pytoh Essencial'}
print(dicionario)  # imprime apenas o que esta dentro da variavel dicionario

print(dicionario['curso'])  # nesse caado aque será impresso o valor da chave curso que esta dentro de dicionario

O DEFAULT DICT NAO GERA ERRO, AO INFORMAR O VALOR ESTAMOS INFORMANDO UM DEFAULT DICT, PODENDO UTILIZR UMA LAMBIDA
PARA ISSO, ESTE VALOR SERA UTILIZADO SEPRE QUE NÃO HOUVER UM VALOR DEFINIDO. E CASO TENTEMOS ACESSAR UM VALOR QUE
NAO EXISTE ESSA CHVE SERÁ CRIADA E O VALOR DEFAULT  SERA ATRIBUIDO

LAMBDAS SÃO FUNÇÕES SEM NOME QUE PODEM OU NAO RECEBER PARAMETROS DE ENTRADA  E RETORNAR VALORES
"""
# fazendo um import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)  # AQUI TEMOS A FUNÇÃO LAMBIDA, QUE NÃO RECEBE NENHUMA ENTRADA E RETORNA ZERO
# print(dicionario)
dicionario['curso'] = 'Programação em Python Essencial'

print(dicionario)
print('Nesse caso o codigo vai criar um outro elemento , e vem com default 0 zero')
print(dicionario['outro'])  # em um dicionário comum erro de chave, nesse caso não
print(dicionario)
