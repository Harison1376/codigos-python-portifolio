"""
Funções com retorno


numeros = [1, 2, 3]  # criação da lista normal

ret_pop = numeros.pop()  # variável recebendo o comando pop

print(f'Retorno de pop {ret_pop}')  # imprimindo a variavel que recebe o resultado de pop  => Retorno de pop 3

ret_pr = print(numeros)  # variável recebendo o novo valor denumeros

print(f'Retorno de print {ret_pr}')  #  imprimindo o valor da variavel que recebeu o valor de numros ja atualizado

OBS: Quando uma função nao retorna nenhm valor, o reotrnoé None

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Exemplo de função

def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()  # Apesar de ter o resultado, isso nao diz que tem retorno, aprenas sendo impresso pelo print

print(f'Retorno de ret:{ret}')

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservado 'return'

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execussão
da função para outra função

[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[

# Vamos refatorar esta função para que ela tenha retorno de valor
def quadrado_de_7():
    return 7 * 7

# Apesar de ter o resultaodo, isso nao quer dizer que tem retorno, aprenas sendo impresso pelo print
# Veja que aqui criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno de ret:{ret}')

# Aqui estou dizendo ao sistema que não use variável e imprima direto o resultado do retorno
print(f'Retorno: {quadrado_de_7() + 1} ')  # podendo ainda realizar uma operação..

]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Refatorando a primeira função
def diz_oi():
    return('oi')  # seu por print aqui vai dar erro de codigo

print(diz_oi())

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função , ou seja, ela sai da execução da função;
# Exemplo 1 -saindo da função
def diz_oi():
    print('Estou sendo executado antes do retorno.....')
    return 'oi'
    print('Estou sendo executado apos o retorno....')  # linha que ão vai ser executada nunca

print(diz_oi())

2 - Podemos ter em uma função diferentes returns;
# Exemplo 2, podemos ter dierentes retornos
def nova_funcao():
    variavel = True  # Variável sendo True
    if variavel:  # Se a variável for True....
        return 4  # imprima 4
    elif variavel is None:  # senão se a a variável for None....
        return 3.2  # retorne 3.2
    return 'b'  # se a variável for False, retorne b

print(nova_funcao())

3 - Podemos em uma função , retornar qualquer tipo de dado e até mesmo multiplos valores;
# Exemplo 3


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Criando uma função para dar cara ou coroa
# Fazendo um import
from random import random

def joga_moeda():
    # Gera um valor numero pseudo_randomico entre 0 e 1
    valor = random()  # refatorando essa função eu tiro essa linha de comando
    if valor > 0.5:  # no lugar onde tem a palavra valor eu coloco um 'random()'
        return 'cara'
    return 'coroa'

print(joga_moeda())




# Erros comuns na utilizalçao de returns, que na verdade não são erros e sim coificação desnecessaria


def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    elif:
        return  False


print(eh_impar())
"""
# Posso limpar o codigo fazendo desa forma que é bem melhor


def eh_impar():
    numero = 5  # Quado eu der a opção de um numero impar por exemplo
    if numero % 2 != 0:  # vai fazer a divisão por 2 e dando valor exato é par, então dara falso
        return True
    return False


print(eh_impar())
