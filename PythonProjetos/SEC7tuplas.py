""""
tuplas (tuple)
Tuplas são bastente parecidas com listas.
Existem basicamente duas diferenças:

1 - Tuplas: são representadas por parenteses () e são mutaveis
2 - As tuplas são imutaveis: isso significa que ao criar um tupla, ela não muda. Toda operação em uma tupla gera nova
    tuplas

# CUIDADO 1:As tuplas são representadas por () parenteses, mais veja:

tupla1 = (1, 2, 3, 4, 5, 6)  # tendo uma vigula não da erro no funcionamento
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)  # isso não é um a tuplas, por nao ter vigula
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # isso é uma tupla por conta de ter virgula
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: podemos concluir que tuplas são definidas pela virgula e não pelo uso do patenteses
(4) ~>não é tupla
(4,) ~> é tupla
4,  ~> é tupla

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tuplas
tupla = ' Harison charles ', ' Progrmação em Python: Essencial'
nome, curso = tupla
print(nome)
print(curso)

# Gera ValeuError se colocarmos um numero diferente para desempacotar
# Métodos para: adição e remoção nas tuplas existem, dado o fato das tuplas serem imutáveis

# Soma*, Valor máximo*, Valor minimo* e tamanho
# Se os valores forem todos inteiros ou reais
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# concatenação de t2 = uplas
tupla1 = (1, 2, 3, )
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(f' Concatenação das tuplas 1 e 2 {tupla1 + tupla2}')

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(f' aqui temos a concatenação da tupla3 {tupla3}')
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2  # tuplas são imutáveis, mais podemos sobrescever seus valores
print(tupla1)

# PODEMOS VERIFICAR SE DETERMINADO ELEMENTO ESTA NA TUPLA
tupla = (1, 2, 3)
print(3 in tupla)  # da pra por um verficador ja dentro do print

# ITERANDO SOBRE UM TUPLA
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# CONTANDO ELEMENTOS DENTRO DE UMA TUPLA
tupla = ('a', 'b', 'c', 'e', 'a', 'b')
print(tupla.count('a'))

nome = tuple('Harison Charles')
print(nome)

print(nome.count('a'))

# O ACESSO DE ELEMENTOS DE UMA TUPLAS TAMBÉM É SEMELHANTE A UMA LISTA
# DICAS PARA  UTILIZAÇÃO DE TUPLAS
# DEVEMOS UTILIZAR TUPLAS TODA VEZ QUE NAO PRICISAR MUDAR DADOS DENTRO DE UMA COLEÇÃO:
# EXEMPLO 1
meses = ('janeiro', 'ferveiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'stembro', 'outubo',  'novmbro,', 'dezembro')

print(meses[5])

# ITERANDO COM while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# VERIFICANDO EM QUAL INDICE M ELEMENTO ESTA NA TUPLA

print(meses.index('junho'))
# ser o elemento não exister, será gerado ValueError

# SLICING
# TUPLA (INICIO,FIM,PASSO)
print(meses[0:])
print(meses[5:])
print(meses[5:9])
print(meses[2:10:2])

# PORQUE USAR TUPLAS?
# TUPLAS SÃO MAIS RAPIDAS QUE LISTAS - IA, CIENCIA DE DADOS, BIG DATES
# tUPLAS DEIXAM O CODIGO MAIS SEGURO

# ISSO PORQUE TRABALHAR COM ELEMENTOS IMUTAVEIS TRAS SEGURANÇA PARA O CODIGO

"""
# COPIANDO TUPLAS
tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de Shallow copy

print(nova)
print(tupla)
outra = (4, 5, 6)
nova = nova + outra

print(nova)
print(tupla)

