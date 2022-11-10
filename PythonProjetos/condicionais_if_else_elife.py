
"""
ESTRUTURAS CONDICIONAIS
if, else, elif


nome = input(" Qual o se nome?")
print(f'Ola {nome}, tudo  me diz uma coisa...')

idade = int(input(' Qual a  sua idade meu caro?'))
if idade < 18:
    print(f" {nome} Posso ver aqui que você tem {idade} , então você é Menor de idade")
    print('Lamentamos, Não posso liberar seu acesso a esse tipo de conteudo.')
else:  # TODO BLOCO COMEÇA DEPOIS DE DOIS PONTOS E NA OUTRO LINHA COM 4 ESPAÇOS.
    if idade > 18:
        print(f'{nome} Voce é maior de idade, vi aqui que você tem {idade}')
        print(f'Seu acesso será liberado em alguns instantes')

"""
ativo = True # Se aqui for false estou dizendo aqui que a ativação da conta nao foi realizada
logado = False
# if ativo is False:  # aqui esta tendo a confirmação de uma não ativação, no modo não pythonco

# MODO PYTHON
if not ativo:  # se não estiver ativo....
# POSSO USAR AINDA ASSIM =: if ativo:
    print('Você precisa ativar sua conta, check seu e-mail por favor')  # caso nao esteja ativo
else:  # senão se estiver ativo...
    print('Bem-vendo ')  # iprima isso
# ativo é True ou False no caso
print(ativo is True)  # vai me dizer se a minnha variavel esta ativa ou falsa

#  POSSO USAR O is DENTRO DE OUTRAS FUNÇÕES
# NOME = 'HARISON'
# nome.isupper()...islower()....istitle()...etc