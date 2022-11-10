"""
Funções com Parãmtros(de entrada)

- Funções que recebem dados para serem processados dentro da mesma:

Se a gente pensar em um programa qualquer, geralmente temos :

- entradas -> processamento -> saida

Se a gente pensar em uma funçõo, já podemos pensar que temos funções que:
- Não possuem entradas
- Não possuem saida;
- Possuem entrada, mais não possouem saida;
- Não possuem entrada, mais possuem saida;
- Possuem entrada e saida


# Refatorando uma função

def quadrado_de_7():
    return 7 * 7

# mesmo que eu repita esta função varias vezes o valor sempre ser o mesmo, pois ela não tem entrada
print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())


def quadrado(numero):  # aqui estou oferecendo um parametro de entrada, TEM QUE SER PASSADO, SENAO DA ERRO
#    return numero * numero  # dizendo que ele vai fazer a operação do numero * o numero que eu passar
    return numero ** 2  # usando outra forma de fazer o quadrado de um numero, ou ao cubo, trocando o valor do numero


print(quadrado(7))  # o que esta entro do parenteses é o que será usado para fazer o calculo
print(quadrado(5))
print(quadrado(2))

ret = quadrado(6)  #  posso passar essa forma de resutado tambem
print(ret)


# REFATORANDO A FUNÇÃO USADO EM DEFINIÇÕES DE FUNÇÃO
def cantar_parabens(aniversariante):
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas feliciadades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')

cantar_parabens('Daniel, ehhhhh')


# Funções podem ter N parametros de entrada, ou seja,  podemos receber como entrada
# em uma função quantos parametros forme necessarios, ele são separados por virgula

# Exemplo

def soma(a, b): # tudo que esta dentro desse parenteses é parãmetro
    return  a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))  # tudo que esta aqui dentro desses parenteses é argumentos, ele é semantico ao parãmtro
print(soma(10, 20))

print(multiplica(2, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Harison '))
print(outra(5, 4, 'Charles '))

# OBS: se a gente informar um numero errado de paramtro ou argumento, teremos typeError


# Nomeando parãmetros, ou seja sendo coerente com quem pode vir a fazer manutenção nesse codigo

def nome_completo(nome, sobrenome):
    return f'Nome completo : {nome} {sobrenome}'

print(nome_completo('Harison ', 'Charles'))


# A diferença entre parãmetros e argumentos
# Parãmetros são variaveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parãmetros importa;

nome = 'Harison'
sobrenome = 'Lourenço'

print(nome_completo(sobrenome, nome))  # haverá uma inversão de dados


# Argumentos nomeados (keyword Arguments)

# caso usemos argumentos do parametros nos agumento para informa-los , podemos utilizar qualquer ordem

print(nome_completo(nome="harison", sobrenome='Charles'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Lourenço', nome='harison'))

"""
# erro comun na utilização do return


def soma_impar(numeros):
    total = 0
    for num in numeros:  # para cada num dentro da lista de nuemeros
        if num % 2 != 0:  # onde o restante da divisão for diferente zero(0)
            total = total + num  # o total que é 0(zero) vai ser somado ao numero
    return total  # esse return não pode estar dentro do bloco do if, senao da erro


lista = [1, 3, 5, 8, 10, 11]  # veja que a lista esta ligada a função de soma_impar() e fora do for
print(soma_impar(lista))
