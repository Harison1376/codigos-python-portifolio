"""
Saindo de loops com break
Funciona da mesma forma em linguagens como C ou Java
Utilizamos um break para sair de loops de maneira projetada

# EXEMPLO 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print(' Saiu do loop')


"""
# EXEMPLO 2
while True:
    comando = input('Digite sair para Sair: ')
    if comando == 'sair':
        break

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print(' Saiu do loop')