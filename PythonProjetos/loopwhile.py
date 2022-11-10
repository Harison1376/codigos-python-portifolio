"""
Loop While

Forma geral

While expressão_booleana:
    //execução do loop

O bloco do while será executada enquanto a expressão booleana for veradeira

Expressão booleana é toda expressão onde o resultado é verdadeira ou falso
Exemplo:
num = 0
num = 5
num < 5

EXEMPLO 1 DE WHILE
num = 1
while num < 10:
    print(num)
    num = num + 1  # critério de parada.
#  Em um loop while, é importante que cuidemos do critério de parada

"""
# EXEMPLO 2 DE WHILE
resposta = ''
while resposta != 'sim':
    resposta = input('Já acaou o exercicio? ')