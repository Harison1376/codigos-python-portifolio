"""
LOOP for
loop => estrutura de repetição
for => uma desa estruturas

em JAVA TEMOS:
for (int i = 0; i < 10; i++) {
    //execute o codigo
}

PYTHON
for item in interavel:
    // execute o loop

Utilzamos loops oara iterar sobre sequencias ou sobre valores iteraveis
Exemplos de iteraveis

- Strings
    nome = 'Harison'
- listas
    lista = [1, 3, 5, 7, 9]
- Ranges
    numeros = (1, 10)

# Exemplo de for 1 (iterando sobre strings
for letra in nome:  # para cada letra dentro da variavel nome, imprima essa letra
    print(letra)

#  Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

"""
# SOBRE O RAGNGE:
# range(valor_incial, valor_final)
# OBS: VALOR FINAL É NÃO INCLUSIVE OU SEJA ELE NAO IMPRIME. SE EU QUIER O ULTIMO PEÇO UM VALOR A MIS
"""
for numero in range(1, 10):
    print(numero)  # dentro desse print vai ser impresse os valores que saem de 1 a 9    


FORMAS DE SE FAZER UM FOR PARA ENUMERATE-INDICE

nome = 'Harison'
lista = (1, 3, 5, 7, 9)
numero = range(1, 10)  # ainda tera que ser transformado numa lista

FORMA 1
for i, v in  enumerate(nome):  # nas variáveis i e v posso usar por exemplo indice, letra
    print(nome[i])  # inde esta a letra i eu coloco a palvra indice  

FORMA 2
for indice, letra in enumerate(nome):  # resumo melhor de se fazer um for para enumerate e indice
    print(letra)
    
FORMA 3  
for _, letra in enumerate(nome):  # como e unumerate me tras indice e valore, eu descarto o indeice com o (_)
    print(letra)
    
OBS: quando nao precisamos de um valor podemos descar usando um underscore

for valor in enumerate(nome):  # Nesse caso me tras o indice e o valor do indice
    print(valor)  # se eu quiser apenas o indeice eu coloco assim => print(valor[i])

********************************************************************************************************************    
qtd = int(input('Qantas vezes esse loop deve rodar'))

for n in range(1, qtd+1):  # estou adicionando o +1 porque senão ele roda apenas 4 vezes
    print(f'imprimindo {n}')
    
qtd = int(input('Qantas vezes esse loop deve rodar'))
soma = 0  # zerando valores

for n in range(1, qtd+1):  # parametrizando com um range
    num = int(input(f'Informe o {n}/{qtd} valor: '))  # Variavel recebe dados conforme usuario e qtd 
    soma = soma + num  # variavel recebe os dados das variaves soma e num e compila
print(f'A soma total é {soma}')  # ja fora do loop for, imprime o que foi alocado dentro da variavel soma
Qantas vezes esse loop deve rodar5
Informe o 1/5 valor: 2
Informe o 2/5 valor: 4
Informe o 3/5 valor: 5
Informe o 4/5 valor: 1
Informe o 5/5 valor: 4
A soma total é 16
  
nome = ' Harison Charels '
for letra in nome:
    print(letra, end='')  # neste caso vai escrever tudo na mesma linha
    
nome = 'harison'
print(nome *3)    
 
"""
# original = U+1F60D
# modificado U0001F60D
for _ in range(3):  # vai exectar
    for num in range(1, 11):  # o num esta dentro do range
      print('\U0001F60D' * num)
