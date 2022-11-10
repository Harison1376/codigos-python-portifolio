"""
RECEBENDO OS DADOS DO USURIO
input: Todo tipo de dado recebido via input é String
Em Python consideramos Strings: tudo que estiver entre:
Aspas Simples
Aspas Duplas
Aspas Simples Triplas
Aspas Duplas Triplas

"""

# ENTRADA DE DADOS
# print("qual o seu nome")
# nome = input().upper() # input significa entrada referente a pergunta do qual os eu nome

nome = input("Qual o seu nome?")
# Exemplo de print antigo, versão 2
# print("seja Bem vindo(a) %s" % nome) # a parcentagem usa o o que esta dentro da varialve nome

# exemplo de print moderno  3.x
# print("seja Bem vindo(a) {0} ".format(nome))  # zero entre chaves usa o o que esta dentro da varialve nome

# EXEMPLO DE PRINT MAIS ATUAL 3.7...
print(f"seja Bem vindo(a) {nome.upper()} ")

# print("Qual a sua idade?")
# idade = input()

idade = int(input("Qual sua idade?"))
# PROCESSAMENTO

# SAIDA DE DADOS

# Exemplo de saida antigo, versão 2.x
# print(" Esta pessoa por nome %s tem %s anos" % (nome, idade)) # esse sinal de % remete a informação ref a respota
# da input, se houver varias variavesi tenho que por
# exemplo de saida moderno 3.x
# print(" Esta pessoa por nome {0} tem {1} anos" .format (nome, idade)) # igual de cima, segue sequencia de valores

# EXEMPLO DE SAIDA MODERNA
print(f"A pessoa por nome de {nome} tem {idade} anos de idade")

# print(f"O sr(a){nome} nasceu em {2021- int(idade)})
print(f"O sr(a){nome} nasceu em {2021 - idade}")  # neste caso passei a formula de calculo para o input
