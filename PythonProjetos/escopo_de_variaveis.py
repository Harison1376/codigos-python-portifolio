"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis Globais;
    - Vaiáveis Globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis Locais;
    - Variáveis Locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    esta limitado ao bloco onde foi declarada.

Para delcarar variável em python, fazemos assim:
nome_da_variavel = valor_da_variavel

Python é uma liguagem de tipagm dinâmica, isso significa que:
ao declararmos uma variável, nós não colocamaos o tipo de dado nela.
Este tipo é inferido ao atribuirmos o valor a mesma

Exempo:
em C
int numero = 42

em Java
int numero = 42


# Reatribuição
numero = 42  # exemplo de variavel global
print(numero)
print(type(numero))

numero = "harison"
print(numero)
print(type(numero))
"""
numero = 42
if numero > 10:  # se a varrável nuemro for maior que que 10
    novo = numero + 10  # Essa é uma varivel local por estar dentro do bloco do if, e sera executada somente aqui
print(novo)
