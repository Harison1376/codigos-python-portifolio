""""
Funções com Parãmetros Padrão (Defaut Parameters)
- Funções inda passagem de parãmtro seja opcional

Exemplo de onde a função da passagem de parãmetro é opcional

print('Harison')
print()

Exemplo de onde a passagem de função é obrigatoria
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())  # vai dar TypeError


# posso personalizar os dos parametros
def exponencial(numero, potencia=2):  # sintaxe padrão caso ue nao informe valorno capa abaixo
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3)) # por padrão eleve ao quadrado, informado padrão na def
print(exponencial(3, 5))  # eleva a pontenia informada pelo usuario

# OBS : Seo ususrio pasar soment 1 parametro, esta será atribuido ao patãmetro numero, e setá calulado quandrado desse
# numero
# Se o ususario passar 2 arguemntos o preieiro seta atribuido ao parãmetro , então sera atribuido o valor informado


# OBS:m Em funções python, os parãmetros com valores defalt DEBEM sempre estar ao final da declaração
# ERRO
def teste(num=2, potencia):  # dá erro por conta de que o valor default nao existe na potencia, so ao contrario da
    return num ** potencia

print(teste(6))


def soma(num1=5, num2=8): # Passando valores padrões para cada condição
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # Daria typeError caso nao fivesse sido definido valores padrões
print(soma())   # Daria typeError caso nao fivesse sido definido valores padrões


# Exemplos mais complexos


def mostra_informacao(nome='harison', instrutor=False):  # estou informando aqui dois padrões nso parãmetros
   if nome == 'harison' and instrutor:
       return 'Bem-vindo instrutor harison!'
   elif nome == 'harison':
       return 'Eu pensei que você fosse o instrutor'
   return f'ola{nome}'


print(mostra_informacao())  # primeira condição se eu nao for nenhum valor será usados os valores padrões do inicio
print(mostra_informacao(instrutor=True))  # segunda condição nome e  instrutor são verade
print(mostra_informacao(True))  # terceira condição, o nome é TRUE e não harison
print(mostra_informacao('Dani'))  # se o nome não é harison e nem TRUE então é Dani
print(mostra_informacao(nome='Daneil'))  # nesse caso eu declarei que no lugar de harison será Daniel

# POR QUE UTILIZAR PARÃMETROS COM VALOR DEFAULT
- Nos permite ser masi flexiveis nas funções
- Evita erros com parãmetros incorretos
- nos perite trabalhar com exemplos mais legiveis de código


# quais tipos de dads podemos utiliazer como valores default para parãmetros
- Qualquer tipode dado:
    - Numeros, Strings, floats, Boolenos, Listas, Dicionários, Funções, collections


# Exemplo de funções como parãmetro


def soma(num1, num2):  # aqui nenhuma novidade, ela vai simplesmente usar dois valos que eu inserir
    return num1 + num2


def mat(num1, num2, fun=soma):  # iniciando com a função soma, se trocar a função ele troca a que esta no retunr
    return fun(num1, num2)


def subtracao(num1, num2):  # nada de anormal aqui tambem apenas sendo realizada uma subtração
    return num1 - num2


print(mat(2, 3))  # recendo os dados da função mat que estava em acordo com a função soma
print(mat(2, 2, subtracao))  # executando a troca de funções da função mat


# ESCOPO - Evitando problemas e confusões

# Variaveis globais
# Variaves locais


instrutor = 'Harison'  # É global pelo fato de ser executado fora de um bloco


def diz_oi():
    instrutor = 'python'   # Variavel local, esta dentro do bloco e será execuda e anula o return
    return f' Ola {instrutor}'


print(diz_oi())

# OBS: SE TIVERMOS UMA VARIAVEL LOCAL COM O MESMO NOME DA GLOBAL A LOCAL TERA PREFERENCIA


def diz_oi():
    prof = 'harison'  # variavel local
    return f' Ola {prof}'

print(diz_oi())

print(prof)  # NameError não é reconhecida, esta fora do bloco


# MUITA ATENÇÃO COM VARIAVEIS GLOBAIS, EVITE O QUANTO PUDER

total = 0


def incremento():
    total = total + 1 # UnboundLocalError (variavel local sendo usada sem ser inicializada)
    return total

print(incremento())
"""




