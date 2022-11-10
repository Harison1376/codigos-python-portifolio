"""
 DENTRO DO CMD EU PRECISO:
 ver se tenho python =. python --version
 FAZER UM UPGRADE=> pip instal --upgrade pip
 INSTLAR DUAS BIBLIOTECAS => pip virtualenv virtualenvwrapper-win


 POSSO TER DUAS OU MAIS VERSÕES DO PYTHON DENTRO DA MINHA MAQUINA, TENHO DUAS FORMAS DE CRIAR PROJETOS NELAS//
# SUPONHAMOS QUE EU QUEIRA CRIAR UM PROJETO NA VERSÃO 3.8.5, POSSO USAR O SEGUINTE COMANDO:
# mkvrtualenv projetoP38 - claro que isso dentro do meu ambiente 3.8.5 #

# desactivate - sai da versão
# rmvirtualenv - remove o ambente virtual

# agora se eu quero quero criar um projeto dentro do ambiente 3.7 eu uso o seuinte comando:
# mkvirtualenv projetoP37 -p python3.7, ou versao similar"""



"""
python.org - vai na parte de documentação  e em pep index"""

"""
Foi comentado sobre pep8 e zen do python
Foi faldo sobre o import this
"""
"""
A Pep8 tem como função nos auxiliar a escrever os códigos em Python de forma bonita e funcional
[1] - Utlizando Camel Case para nome de classes

class Calculadora:
    pass

class CalculadoraCientifica:
    pass
    
    - Sempre dar duas linhas em branco na questão de comentarios
    
    
[2] - Utilize nomes minusculos, separados por undescore para funções ou variaveis

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação  (NESSA VERSÃO JA ESTA DANDO MAIS PRESTE ATENÇÃO)

if 'a' in 'banana':  # se tem a letra 'a' na palavra banana...
    print('tem sim')  # imprima....

[4] - Lihas em branço entre classes e Definições com duas linhas e Métodos dentro de uma lcasse devem ser separados
com uma unica linha

class Calculadora:
    pass

class CalculadoraCientifica:
    pass
    
[5] - Imports devem ser sempre fetos em linhas separadas

#Errado
import sys.os

#CORRETO
impor sys # pacote completo
import os # pacote completo

# Não ha problemas em utilizar
# from types import em StringType, ListType

# varios imports de varios pacotes recomendado:
from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)
 # IMPORTS DEVEM SER SEMPRE COLOCADOS NO TOPO DO ARQUIVO, LOGO DEPOIS DE QUAISQUER COMENTARIOS OU STRINGS
 #E ANTES DE CONSTANTES OU VARIAVES GLOBAIS

[6] - Espaços em expressões e instruções

# Não faça:
funcao ( algo[ 1 ], {outro: 2})


# Faça:
funcao(algo[1], {outro:2})


# Não faça:
a1lgo (1)

# Faça:
algo(1)


# Não faça:
dict ['chave'] = lista [indice]

# Faça:
dict['chave'] = lista[indice]

# Não faça:
x              =1
y              =3
variavel_longa = 5

# Faça:

x = 1
y = 3
varialvel_longa = 5

[7] - Termine sempre uma nova instrução com uma nova linha


"""

