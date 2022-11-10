"""
Tipo String
em Python, um dado é considerado um tipo string, quando;
- Estiver entre aspas duplas, simpes, triplas e  seja qual for a informação que for, ainda que sejam numeros,
  boolenos, etc..

nome = "Harison"
print(nome)
print(type(nome))

nome1 = "Gina's Bar"
print(nome1)
print(type(nome1))

nome2 = "Harison \nCharles"
print(nome2)
print(type(nome2))

nome3 = 'Harison
Charles'
print(nome3)
print(type(nome3))

nome = "Harison Charles"
print(nome.upper())  # Impressao do nome tudo em caixa auta
print(nome.lower())  # Impressao do nome tudo em caixa baixa
print(nome.split()) # Transforma o nome em uma lista de strings


print(nome[0:7])  # a posição 7 é o espaço, mais se eu pegar ate a 6 eu perco a letra n do nome, temos aqui uma slice
print(nome[8:15])  # Tanto na configuraçã acima quanto nesssa temos uma slice de string

#  [  0  .       1    ]
# 'Harison' , 'Charles'
print(nome.split()[0])  # vou acessar o primeiro nome, ou seja  lista 1
print(nome.split()[1])  # vou acessar o segundo nome , ou seja lista 2

# Imprimindo de tras pra frente
print(nome[::-1])  # Comecedo ultimo elemento e vá ate o primeiro invertendo a ordem
"""
# [ 0,  1,    2,   3,   4,   5,   6,   7,  8,   9,   10,  11,  12,  13,  14]
# ['H , 'a', 'r', 'i', 's', 'o', 'n', ' ' 'C', 'h', 'a', 'r', 'l', 'e', 's']
nome = "Harison Charles"
print(nome.replace('H', 'F'))  # Substituindo uma lera por outra

texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])
