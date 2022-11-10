"""
LISTAS (list)

Listas em python funcionam como vetores/ matrizes (arrays) em outras linguagens,  com a diferença de serem
DINÂMICAS,  e também de podermos colocar QUALQUER TIPO DE DADO

lingegens C/JAVA: arrays
    - possuem tamnanho fixo:
    Ou seja, nestas linguagens se for criado um array de tipo inte e com tamnaho 5, sera sempre do mesmo tamanho ,
    sempre do tipo inteiro e poderá ter SEMPRE no maximo 5 valores

Já em Python
- Dinâmico: não possuem tamanho fixo; ou seja podemos criar a lista e simplmente ir acrescedo nela elementos;
- Qualquer tipo de dado; As listas não posseum tipo de dado fixo ou seja podemos colocar qualquer tipo de dado

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
As lisas em python são representados por colchetes []
AS LISTA EM PYTHON, SÃO MUTÁVEIS, OU SEJA  PODEM SER MUDADAS

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['h', 'a', 'r', 'i', 's', 'o', 'n', ' ', 'c', 'h', 'a', 'r', 'l', 'e', 's']

lista3 = []

lista4 = list(range(11))

lista5 = list('Harison Charles')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# podemso facilmente checar se determinado valor esta contido na lista.
num = 45
if num in lista4:  # Aqui vai dar negativo pois nao existe o numero procurado
    print(f'numero {num} achado')
else:
    print(f'numero {num} nao encontrado')

# PODEMOS FACILMENTE ORDENAR UMA LISTA
lista1.sort()
print(lista1)

# podemos facilmente contar o numero de ocorrencias de um valor em uma lista - MUITO IMPORTANTE
print(lista1.count(1))  # ESTE COMANO NÃO É COMO O Counter, que conta e enumera as ocorrencias de uma chave
print(lista5.count('e'))

# adicionar elementos em uma lista
"""
# PARA ADIDIONAR VALORES OU ELEMENTOS EM UMA LISTA Á UMA LISTA USAMOS A FUNÇÃO -> append

"""
print(lista1)
lista1.append(56)
print(lista1)

# COM append, nós so conseguimos adicionar um elemento por vez
# lista1.append(34, 45, 67)  # vai dar erro,

# É POSSIVEL
print(lista1)
lista1.append([9, 2, 7])  # COLOCA A LISTA COMO ELEMENTO UNICO
print(lista1)
print(lista1.count(3))
if [9, 2, 7] in lista1:
    print('encontrei a lista')
else:
    print('nao achei a lista')

# POSSO ADICIONAR VALORES A LISTA PELO extend
lista1.extend([123, 59, 89])  # ADICIONA ELMENTOS A LISTA COMO VALORES ADICIONAIS
print(lista1)

# PODEMOS INSERIR UM ELEMENTO A LISTA INFORMANDO A POSIÇÃO DO INDICE
# NÃO SUBSTITUI, APENAS DESLOCA PARA A DIREITA DA LISTA.
lista1.insert(2, 'HCL')  # numero 2 indica a posição do indcie e as letras o que vai entrar no lugar do indice.
print(lista1)


# PODEMOS FACILMENTO JUNTAR DUAS LISTA, SÓ QUE NESSE CASO ESTOU CRIANDO UMA NOVA LISTA
lista6 = lista1 + lista2
print(lista6)

# NESSE CASO NÃO PRECISO CRIAR NENUM OUTRA VARIÁVEL
lista1.extend(lista2)
print(lista1)

# PODEMOS FAZER IMPRESSÃO DAS LISTAS AO INVERSO
# FORMA 1 DE REVERSÃO
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# POSSO USAR AINDA O SLICE , OU SEJA MESMA REVERSÃO
# FORMA 2 DE REVERSÃO
print(lista1[::-1])
print(lista2[::-1])

# COPIANDO UMA LISTA  # Deep copy
lista6 = lista1.copy()
print(lista6)

# VENDO O TAMANHO DE UMA LISTA
print(len(lista4))  # mostra o tamanho da lista

# PODEMOS REMOVER FACILMENTE O ULTIMO ITEM DE UMA LISTA
# O POP NAO SOMENTE REMOVE O ULTIMO ELEMENTO COMO TAMBEM RETORNA O VALOR REMOVIDO
print(lista5)
lista5.pop()
print(lista5)

# PODEMOS REMOVER UM ELEMENTO PELO INDICE
# OS ELEMENTOS A DIREITA SÃO DESLOCADOS PARA A ESQUERDA
lista5.pop(2)
print(lista5)

# PODEMOS AINDA REMOVER TODOS OS ITENS DA LISTA
print(lista5)
lista5.clear()   # limpa toda a lista
print(lista5)

# PODEMOS FACILMENTE REPETIR ELEMENTOS EM UMA LISTA
nova = [1, 2, 3]
nova = nova * 3
print(nova)

# PODEMOS CONVERTER UMA STRING PARA UMA LISTA
# exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()  # convertendo string em lista por padrão ele usa o espaço entre elas.
print(curso)
print(curso.count('em'))  # quantos elementos dentro da lista
print(len(curso))   # tamanho da lista

# EXEMPLO 2 CONVERTENDO UMA STRING PARA LISTA COM SPLIT
curso = 'Programação,em,Python:,Essencal'
print(curso)
curso = curso.split(',')  # esetou usando a virgula como parametro de divisão entre os caracteres
print(curso)

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# CONVTENDO UMA LISTA EM STRING
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# abaixo estamos falando, pega a lista6 coloca espaço em cada elemente e transforma numa string
curso = ' '.join(lista6)  # tem que ser dado o espaço dentro das aspas
print(curso)

# abaixo estamos falando, pega a lista6 coloca cifrão entre entre cada elemente e transforma numa string
curso = '$'.join(lista6)
print(curso)

# PODEMOS COLOCAR REALMENTE QUALQUER TIPO DE DADO DENTRO DE UMA lista, INCLUSIVE MISTURANDO DADOS
lista6 = [1, 2.34, True, 'Harison', 'd', [1, 2, 3], 5422645754]
print(lista6)
print(type(lista6))

# ITERANDO SOBRE LISTAS
# EXEMPLO 1 UTILIZANDO for

soma = 0  # => SE FOSSE PRA TER UMA SOMA DE STRING TERIA QUE TER ASPAS VAZIAS <=
for elemento in lista1:  # NOTE QUE NÃO PRECISA DE VARIAVEL PRA PODER ALOCAR O QUE VAI SER IMPRESSO, SO PEDIR
    print(elemento)  # VAI IMPRIMIR CADA ELEMENTO DENTRO DA LISTA.
    soma = soma + elemento
print(f' Valor tota dentro a lista é: {soma}')

# EXEMPLO 2 UTILIZANDO while

carrinho = []  # criada lista vazia
produto = ''  # dados que serão digitados pelo usuario

while produto != 'sair':  # enquanto for diferente de sair
    print("Adicone um produto a lista ou digite 'sair' para sair:  ")  # imprima
    produto = input()  # o produto digitado pelo usuario
    if produto != 'sair':  # se o prdoduto for diferente de sair
        carrinho.append(produto)  # adicione o produto ao carrinho digitado pelo usuario 

for produto in carrinho:  # para cada produto dentro do carrinho.
    print(produto)  # imprima o produto 
    
# UTILIZANDO VARIAVES EM LISTA
numeros1 = [1, 2, 3, 4, 5]  # aqui essa varieavel contem uma lista dentro dela
print(numeros1)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros2 = [num1, num2, num3, num4, num5]
print(numeros2)

# PODEMOS TER ACESSO AOS ITENS DE FORMA INDEXADA

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# PODEMOS AINDA FAZER ACESSO AOS ELEMENTOS DE FORMA INDEXADA AO CONTRÁRIO
# PARA ENTENDER O INDICE NEGATIVO, PENSE NA LISTA COMO UM CIRCULO, ONDE TERMINA UM COMEÇA O OUTRO
# o final de um elemento esta ligado ao inicio da lista

print(cores[-1])  # vai imprimir a cor branca
print(cores[-2])   # vai imprimir a cor zaul
print(cores[-3])  # Vai imprimir a cor amarelo
print(cores[-4])  # Vai imprimir a cor verde
# print(cores[-5])  # Vai dar erro, não temos o indeice -5

for cor in cores:
    print(cor)

indice = 0  # Variável indice começando em zero
while indice < len(cores):  # enquanto o indice for menor que o tamanho de cores dentro da tabela
    print(cores[indice])  # imprima a cor no seu indice
    indice = indice + 1  # somando esses indices mais 1 ate dar o tamanho da lista
    
# Gerar indice em um for
for indice, cor in enumerate(cores):  # gera pares e valores, ou seja coloque o indice e o valor desse indice
    print(indice, cor)  # preste atenção na hora de preencher este campa pois pode gerar conflito
    
# LISTAS ACEITAM REPETIÇÃO
lista = []
lista.append(3)
lista.append(43)
lista.append(43)
lista.append(33)
lista.append(33)
lista.append(10)
print(lista)
print(len(lista))
print(lista.count(43))


# MÉTODOS NAO TÃO IMPORTANTES MAIS USADOS EM LISTA

# ENCONTRAR O INDICE DE UM ELEMENTO NA LISTA
# EM QUAL INDICE DA LISTA ESTA O VALOR 6
numeros = [5, 6, 5, 7, 8, 9, 10]
print(numeros.index(6)) vai mostora que o numero 6 esta no indice 1

# EM QUAL INDICE ESTA O VALOR 9
print(numeros.index(9))

# CASO NÃO HAJA O ITEM NA LISTA, ESTE APRESENTA ERRO > VallueError
# print(numeros.inedex(19))

# OBS: CASO EU TENHA VALORES REPTIDOS DENTRO DA MINHA LISTA.....
print(numeros.index(5))   # vai retornar o indice do primeiro elemento encontrado

# podemos fazer busca dentro de um range, ou seja, qual o indice começar a buscar
print(numeros.index(5, 1))  # ENCONTRE O NUMERO 5 DENTRO DO RANGE A PARTIR DO INDICE 1
print(numeros.index(5, 2))  # ENCONTRE O NUMERO 5 DENTRO DO RANGE A PARTIR DO INDICE 2
# CASO NÃO HAJA O ITEM NA LISTA, ESTE APRESENTA ERRO > ValueError

# PODEMOS FAZER BUSCA DENTRO DE UM RANGE INICIO E FIM
print(numeros.index(7, 2, 6))  # busque o valor 7 entre os indices 2 a 6

#  REVISANDO SLICE - VISTO EM STRING
# lista[incio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice  de lista com parametro de inicio
lista = [1, 2, 3, 4]
print(lista[1:])  # Iniciando no indice 1 e pegando todos os elementos restantes
print(lista[::])  # pegando todos os elementos da lista

# Trabalhando com slice  de lista com parametro de fim
print(lista[:2])  # começa em 0, pega o indice 2-1
print(lista[:4])  # começa em 0, pega o indice 4-1
print(lista[1:3])  # começa em 1, pega o indice 3-1

# trabalhando com slice de lista com o parametro passo
print(lista[1::2])  # Começa em 1, vai ate o final de 2 em 2

print(lista[::2])   # começa em 0, vai ate o fim de 2 em 2

#INVERTENDO VALORES DENTRO DE UM LISTA

nomes = ['Harison', 'Charles']
nomes[0], nomes[1] = nomes[1], nomes[0]  // ADQUI ESTOU INVERTENDO PELO INDICE
print(nomes)

nomes = ['Harison', 'Charles']  # pra eu poder fazer isso tenho de ter a variavel com a lista dentro.
nomes.reverse()
print(nomes)


# Soma*, Valor Máximo*, Valor Minimo*, Tamanho
# * neste casos os valores precisam ser inteiros  ou reais ou seja ponto flutuante
lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma lista
print(max(lista))  # Maximo valor
print(min(lista))  # Minimo valor
print(len(lista))  # Tamnho da lista

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# DESEMPACOTAMENTO DE LISTA, LEMBRANDO QUE NAO HAVENDOO ELEMENTO ACARRETA EM ERRO

lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)


"""

# COPIANDO UMA LISTA PARA OUTRA - (SHALLOW  E DEEP COPY)
# DESEMPACOTAMENTO DE LISTA, LEMBRANDO QUE NAO HAVENDOO ELEMENTO ACARRETA EM ERRO
# forma 1
#
print('aqui temos exemplo de DEEP COPY')

lista = [1, 2, 3]
print(f'imprimindo a primeira lista {lista}')

nova = lista.copy()
print(f'imprimindo a copia da nova lista{nova}')

nova.append(4)

print(f'imprimindo novamente a lista inicial {lista}')
print(f'essa é a lista nova com append  {nova}')

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para a anova lista. mas elas ficaram totalemente
# independentes, ou seja, modificando uma lista, nao afeta a outra. Isso em Pthon é Deep copy, ou seja copia profunda
print('Aqui temos exemplo de SHALLOW COPY')

lista = [1, 2, 3]
print(f' novamente a lista incial {lista}')

nova = lista  # por conta de não fazer o copy() eu abro parametros para uma lista ser alterada junto com a outra

nova.append(4)

print(f' imprimindo a lista inicial{lista}')
print(f' imprimindo a lista nova {nova}')

# Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista, mais após ralizar as
# modificações em um das listas essa modificação refletiu nas duas. Isso em Python  é chamada de Shaloow copy

# abaixo estamos falando, pega a lista6 coloca espaço em cada elemento e transforma numa string
lista6 =['Harison', 'Charles ', 'lourenço']
curso = ' '.join(lista6)  # tem que ser dado o espaço dentro das aspas
print(curso)
