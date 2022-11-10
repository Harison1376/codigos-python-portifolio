"""
Definindo funções.
- Funções são pequenas trechos de codigo que realizam tarefas especificas.
 - Pode ou não receber entradas de dados e retornar uma saida de dados
  - Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Escrevendo uma função que realiza varias tarefas dentro dela;
 - é bom fazer uma verificação para que a função seja simplificada.

- Ja utilizamos varias funções desde que iniciamos esse curso:
-print()
-len()  define tamanho
- max() define numero maximo ou maior
- count() conta a quantidade de itens dentro de uma tupla, lista, etc...
- e muitas outras

    Exemplo a função print() que é imprimir aquilo que colocamos dentro de um comando

"""
# exemplo de utilização de funções

# cores = ['verde', 'amarelo', 'azul', 'branco']

# utilizando uma função ja integrada no python - built-in
# print(cores)  # dado de entrada é cores print é a função
# curso = ('Programação  em Python: Essencial')

# print(curso)  # dado de entra é o curso

# cores.append('roxo')  # o appende é uma função dentro da lista
# print(cores)

# curso.append('mais cursos.....')  # gera um erro por conta de que o append aloca apenas um item por vez e não texto
#  print(curso)
# cores.clear() # O clear também é uma função dentro de lista
# print(cores)

# print(help(print))
# DRY - Don't Reapet Yoursel => Não reprita você mesmo / Não repita seu código

# MAIS ENTÃO, COMO DEFINIR FUNÇÕES.....
"""
EM Python a forma geral de definir uma função é:
def nome_da_função(parametros_de_entrada):
    bloco_da_funcao
    
 Onde:
 nome_da_funcao -> sempre com letras minusculas e se for composto: separado por undescore(snake Case) 
 Parametros _de_entrada -> opcinais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não
 ou seja com o que a função vai trabalhar, é o que esta entre parenteses
 
 Bloco_da _funcao -> também chamdo de corpo da função ou implementação, é onde o processamento da função acontece.
 Neste bloco, pode ter o não retorno da função
 
OBS: Veja que para definir uma função utlizamos a palavra  resevada 'def' informando para o Python que estamos 
definindo uma função. Também ja abrimos o bloca de codigo com o ja conehcido dois pontos. Que é usado em Python para
definir blocos.
"""
# Definindo a primeira função
# Definição
def diz_oi():  # Fiz a definição da função, não passei nenhum paremetro e indiquei a abertura de um novo bloco
    print('oi!')  # solicitei a execução de uma função built-in o print

"""
OBS: 
1 - Veja que, dentro das nossas funções podemos utilizar  outras funções;
2 - Veja que, nossa função executa apenas 1 tarefa, ou seja a unica coisa  que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parametro de entrada;
4 - Veja que esta função não retorna nada;

"""
# Utilizando funçoes

# Chamada da execução
diz_oi()  # NAO PODE HAVER ESPAÇO E SEM O PARENTESES NAO EXECUTA A FUNÇÃO, E VEJA AINDA QUE NAO TEM OS DOIS PONTOS

# EXEMPLO DOIS

def cantar_parabens():
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas feliciadades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')


cantar_parabens()  # posso ainda imprir isso 4 vezes ou fazer um range

# for n in range(5):  # Para cada vez que rodar dentro de 5 vezes
#   print(n)  # apenas quero imprimir a quntidade de vezes impressa, não tem necessidade de usar variável
#  cantar_parabens()  # Execute o cantar parabens.

# Em Python, podemos inclusive criar variavesde tipo de uma função e executar esta função atraves a variável
# Lembando que não é comun em outras linguagens, e ate mesmo em Python não se usa muito.
canta = cantar_parabens  # Defini a variavel de alocação da função, e coloque dentro dela a função

canta()  # Aqui estou executando a função

