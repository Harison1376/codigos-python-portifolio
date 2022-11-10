"""
ESTRUTURAS LOGICAS and(e), or(ou), not(nao), is(e)

OPERADORES UNAÁRIOS
  - not, is

OPERADORES BINÁRIOS
  - and, or
REGRAS:
para and - ambos valores precisam ser verdade
para or - um outro valor precisa ser verdade
para not o valor do booleano é invertido, ou seja onde for True vira False, ser for False vira True


usuario = input(" Digite seu nome")
ativo = True
logado = True
if ativo and logado:  # PARA and ambos valores são verdade, ja se for or um ou outro precisa ser verdade.
    print(f' Bem vindo {usuario}')
else:
    print(" Uuário nao encontrado, favor verificar seu e-mail e confirmar cadastro")
"""
usuario = input(" Digite seu nome")
ativo = True
logado = False
if not ativo:  # ou seja se nao for True.. isso depois da confirmação de e-mail
    print('Você precisa checar seu e-mail')
else:
    print('Bem vindo')