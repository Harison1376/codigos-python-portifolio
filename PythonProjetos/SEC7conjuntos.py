"""
Conjuntos: em qualquer linguagem de programação estamos fazendo referencia a teoria dos conjuntos da matematica

Aqui em Python os conjuntos são chamados de Sets

Dito isso, da mesma forma que na matematica
Sets (conjuntos) - não possuem valores duplicados
Sets (conjuntos) - não possuem valores ordenados
Sets (conjuntos) -  não são acessados via indice, ou seja, conjuntos nao são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos , mas não nos impotamos com a ordenação deles
Quando nao precisamos nos preocupar com chaves valores e itens duplicados

Os conjuntos Sets, são referenciados em python com chaves {}

Diferença entre conjuntos (Sets) e mapas (dicionários)
    - Um dicionário tem chave e valor
    - Um conjunto (set) tem apenas valor


# definindo um conjunto. O FATO DE POR A PALAVRA 'set' DEPOIS DO SINAL DE IGUAL DA VARIAVEL JA DIZ QUE É CONJUNTO.
# forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos aqui valores repetidos

print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja add um valor ja existente o mesmo será ignorado, sem gerar erros e nao fara
# parte do conjunto.


# forma 2 - mais comum

s = set({1, 2, 3, 4, 5, 5})
print(s)
print(type(s))

# CONVERTENDO UM SET PARA LISTA
d = 'Harison Charles' # gerando string normalmente
print(d)

d = set('Harison Charles')  # Quando for feito o 'set' as letras que estão repetidas não vao aparecer
print(d)
print(type(d))

# podemos verificar se determinado elemento esta contido no grupo

if 3 in s:
    print('tem o 3')
else:
    print('não tem o 3')


# Importante lembrar que alem de não termos valores dupicados, não temos ordem

# lISTAS ACEITAM VALORE DUPLICADOS, TEMOS ENTÃO 10 ELEMENTOS
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} com {len(lista)} elementos')

# TUPLAS ACEITAM VALORE DUPLICADOS, TEMOS ENTÃO 10 ELEMENTOS
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'tupa: {tupla} com {len(tupla)} elementos')

# DICIONARIOS NÃO  ACEITAM VALORE DUPLICADOS, TEMO ENTÃO 8 ELEMENTOS => TEM CHAVE E VALOR
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')  # tem que ter o {}.fromkeys
print(f'dicionario: {dicionario} com {len(dicionario)} elementos')  # NÃO REPETE VALORES

# CONJUNTOS NÃO ACEITAM VALORE DUPLICADOS, TEMO ENTÃO 8 ELEMENTOS  POIS NAO TEM CHAVE
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f' Conjunto: {conjunto} com {len(conjunto)} elementos')


# COMO TODO OUTRO CONJUNTO PYTHON PODEMOS COLOCAR TODOS OS TIPOS DE DADOS MISTURADOS EM Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# PODEMOS ITERAR EM UM Set NORMAMLMENTE

for valor in s:
    print(valor)


# USOS INTERESSANTES COM sets
# IMAGINE QUE FIZEMOS FORMULARIO  DE CADASTRO DE VISITEANTES EM UMA FEIRA  OU MUSEU, ONDE OS VISITANTES INFORMAM A
# CIDADE DE ONDE VIERAM
# NÓS ADICIONAMOS CADA CIDADE EM UMA LISTA PYTHON, JA QUE EM LISA PODEMOS ADICIONAR NOVOS ELEMENTOS E TER REPETIÇÃO

cidades = ['Belo horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# AGORA PRECISAMOS SABER QUANTAS CIDADES DISTINTAS TEMOS , OU SEJA UNICAS CIDADES
# O QUE PODEERIA SER FEITO? UM LOOP NA LISTA?
# PODEMOS UTILIZAR O set PARA ISSO...

print(len(set(cidades)))  # vou trasnsformar a lista em um set e ele vai eliminar as cidades repetidas

# ADICIONANDO ELEMENTOS EM UM CONJUNTO
s = {1, 2, 3 }
s.add(4)
s.add(4)  # dupliciade não gera erra, simplesmente é ignorado e não adiciona o valor
print(s)

# REMMOVENDO  ELEMENTOS EM UM CONJUNTO
s = {1, 2, 3 }
print(s)

# forma 1
s.remove(3)  # nao  é indice e sim valor, informamos o valor a ser removido
print(s)

# obs: caso valor nao seja encontrado, será gerado um erro KeyError

# forma 2

s.discard(2)  # no caso do discard,nao tendo o valor, não gera erro,
print(s)

# COPIANDO UM CONJUNTO PARA OUTRO....

s = {1, 2, 3}

# forma 1 Deep Copy
# nova variavel recebendo uma copia de s
novo = s.copy()
print(novo)

# adicinando um novo valor ao conjunto
novo.add(4)
# imprimindo a variavel novo e a variavel s para comparação
print(novo)
print(s)

# forma 2 Shallow Copy
novo = s  # em Python estou dizendo que estas duas variaves terão o mesmo valor

novo.add(4)

print(novo)
print(s)

# Podemos remover toso os itens de um conjunto

s.clear()  # vai limpar tudo o que estiver dentro do conjunto.
print(s)


# Métodos matematicos de conjuntos

# Imagine que temos dois conjuntos: um contendo estudantes do curso de Python e um contendo estudantes do curso de Java
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Ferando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# veja que alguns alunos que estudam python também estudam Java
# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union  RECOMENDADO

unicos1 = estudantes_python.union(estudantes_java)
# {'Ferando', 'Guilherme', 'Gustavo', 'Julia', 'Patricia', 'Marcos', 'Pedro', 'Ana', 'Ellen'}
# unicos1 = estudantes_java.union(estudantes_python)
# {'Guilherme', 'Ana', 'Ellen', 'Pedro', 'Julia', 'Patricia', 'Gustavo', 'Marcos', 'Ferando'}
print(unicos1)

# Forma 2 - Utilizando caractere pipe |, essa barra em pé

unicos2 = estudantes_python | estudantes_java
# {'Ferando', 'Marcos', 'Ana', 'Patricia', 'Ellen', 'Guilherme', 'Gustavo', 'Julia', 'Pedro'}
print(unicos2)



# PRECISAMOS GERAR UM CONJNTO DE ESTUDANTES QUE ESTÃO EM AMBOS OS CURSOS
# Forma 1 - Utilizando o intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o & ( E comercial)
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que nao estão no outro
# UTILIZANDOO difference

so_pthon = estudantes_python.difference(estudantes_java)
print(so_pthon)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

"""
# Soma, Valor Maximo*, Valor Minimo*, Tamanho  para valores inteiros e reais

s = {1, 2, 3, 4, 5, 6}
print(f' A Soma total do conjunto  é : {sum(s)}')
print(f' O maior numero do conjunto é: {max(s)}')
print(f' O menor  numero do conhjunto é: {min(s)}')
print(f' O tamnho dessse conjunto é : {len(s)}')


# CONJUNTOS NÃO ACEITAM VALORE DUPLICADOS, TEMO ENTÃO 8 ELEMENTOS  POIS NAO TEM CHAVE
conjunto = {}.fromkeys({99, 2, 34, 23, 2, 12, 1, 44, 5, 34}, 'dict')
print(f' Conjunto: {conjunto} com {len(conjunto)} elementos')
