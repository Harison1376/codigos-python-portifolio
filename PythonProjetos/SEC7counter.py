"""
Módulo Collections - Counter (contador)  é um tipo estendido dentro de collections

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performance Container Datetypes
               Tipos de daddos de container de alta performance

Counter -> Recebe um iteravel com o parametro e cria um obbjeto do tipo collections que é parecido com um dicionário
contendo como chave o elemento da lista passado como parametro e como valor a quantidade de ocorrencias desse elemento



# Realizando o import
from collections import Counter

# Exemplo 1
# Podemos utilizar qualquer iteravel, neste caso estamos utilizano uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5,  5,  5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o counter

res = Counter(lista)  # criado uma variavel para receber o resultado do Counter lista

print(type(res))

print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})  # Esse é o resultado
# Para cada elemento da lista ele criou uma chave e colocou como valor a quantidade de ocorrencias

# Exemplo 2
# Realizando o import
from collections import Counter
print(Counter('Harison Charles Lourenço'))

#Counter({'r': 3, 'o': 3, 'a': 2, 's': 2, 'n': 2, ' ': 2, 'e': 2, 'H': 1, 'i': 1, 'C': 1, 'h': 1, 'l': 1, 'L': 1, 'u': 1, 'ç': 1})

"""
from collections import Counter  # preciso ante de usar o COUNT importar a biblioteca dele
# Exemplo 3
texto = """Banhado pelo Oceano Atlântico, o Brasil tem um litoral de 7 491 km[12] e faz fronteira com todos os outros
países sul-americanos, exceto Chile e Equador, sendo limitado a norte pela Venezuela, Guiana, Suriname e pelo
departamento ultramarino francês da Guiana Francesa; a noroeste pela Colômbia; a oeste pela Bolívia e Peru; a
sudoeste pela Argentina e Paraguai e ao sul pelo Uruguai. Vários arquipélagos formam parte do território brasileiro,
como o Atol das Rocas, o Arquipélago de São Pedro e São Paulo, Fernando de Noronha (o único destes habitado por
civis) e Trindade e Martim Vaz.[12] O Brasil também é o lar de uma diversidade de animais selvagens, ecossistemas
e de vastos recursos naturais em uma grande variedade de habitats protegidos."""

palavras = texto.split()  # Transforma todo o texto em lista.

# print(palavras)

res = Counter(palavras)
print(res)

# Mostrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))  # imprima o resultado da variavel res e me diga as cinco palavras mais comuns

