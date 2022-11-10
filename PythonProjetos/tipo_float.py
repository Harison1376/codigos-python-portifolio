"""
Tipo float
Tipo Real, decimal

Casas decimais

OBS: O separador de casas decimais é o ponto e não a vigula

# Errado do ponto de vista float, mais gera uma tupla
valor = 1,44  # aqui temos uma tupla
print(valor)
print(type(valor))

# Certo do ponto de vista foat
valor0 = 1.44
print(valor0)
print(type(valor0))

# Podemos fazer dupa atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
res = int(valor0)
print(res)
print(type(valor0))


# Podemos ainda utilizar nuemeros complexos
num = 5j  # Numeros complexos
print(num)
print(type(num))

# Conversoão de inteiro para float
num = 1_000_000
print(num)
print(float(num))

"""
# Imprimindo de uma forma a ser entendida
salario = 160.66
salario1 = 200.55
total = salario + salario1
print(total)
print(type(total))

# impressão que pode ser incorreta
total2 = int(salario) + int(salario1)
print(total2)
print(type(total2))
