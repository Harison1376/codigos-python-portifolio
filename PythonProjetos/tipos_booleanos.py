"""
Tipo Booleano vem do nome de seu criador George Boole

Sempre com duas constantes, Verdadeiro ou Falso
True    Verdadeiro
False - False
"""
# Testando Usúario
ativo = True  # A lógica por detras disso é que ele vai fazer uma conferencia se sim ou nao, seu eu colocar False muda
print(ativo)  # será impresso o que a variavel esta dizendo que é... nessse caso é verdade

"""
Operações basicas
"""

# negação not

"""
Fazendo a negação, se o valor for verdadeiro o resultado sera falso , se for falso o resultado sera veradeiro, ou seja,
sempre o contrario
"""

print(not ativo)

# Ou (or)

logado = False
"""

e uma operação binária, ou seja, uma ou outra deve ser verdadeira, depende sempre de dois valores

True or True = True
True or False = True
False or True = True
False or False = False

"""
print(ativo or logado)

# Operação E (and):

"""
Também uma operação binaria, onde os dois valores precisam ser verdadeiras
True or True = True
True or False = False
False or True = False
False or False = False
"""
# Posso até mesmo usar operação booleana

"""
>>> 5>6
False
>>> num = 10
>>> num2 =8
>>> num3 = 6
>>> num > num3 < num2
True

>>> num = 10
>>> num2 =8
>>> num3 = 6
>>> num > num3 < num2
True
>>> num and num3 > num2
False
>>> num and num2 > num3
True

"""
print(type(True))  # Vai imprimir pra mim que isso é uma classe booleanas
