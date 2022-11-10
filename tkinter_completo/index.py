# DO TKINTER IMPORTE TUDO;  ESSE É  PRIMEIRO PASSO*****************************
from tkinter import *
from tkinter import ttk  # IPORTANTANDO A BIBLIOTECA TTK; VAI DAR SUPORTE AS JANELAS
import sqlite3  # IMPORTANDO FUNÇÕES DO BANCO DE DADOS

# SEGUNDO PASSO ***********************************************
# ABRINDO A JANELA, LEMBRANDO QUE ELA ESTA FORA DAS APLICATIONS(), POR ISSO CRIO UMA INSTANCIA DENTRO DA APLICATION.
root = Tk()

# criando uma classe para inserir minha função limpa_tela, não precisa de _init_ o application fara isso como parâmetro


class funcs():  # criada para limpar as entrys
    def limpa_tela(self):
        # função delete vai apagar quando eu chamar, neste caso não precisa ser alocada no _init_, carrega sozinha
        # limpa da linha  até o final da entry codigo
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)  # limpa entry nome
        self.fone_entry.delete(0, END)  # limpa entry
        self.cidade_entry.delete(0, END)

    # Criando banco de dados =>NAO PRECISA CHAMAR NO INIT JA ESTA DENTRO DO MONTA_TABELA
    def conecta_bd(self):  # criando a função chamando o banco de dados
        # variável para charmar o sqlite3 para conectar bd
        self.conn = sqlite3.connect('clientes.db')
        self.cursor = self.conn.cursor()  # resume a função e facilita o trabalho
        print('conectando ao banco de dados')
    # função de desconecção do banbo
    # ESSA FUNÇÃO DO DESCONECTA JA ESTA DENTRO DO MONTA TABELAS, NAO PRECISA CHAMAR NO INIT

    def desconecta_bd(self):  # Vai desconectar o banco depois de uma chamada
        self.conn.close()  # essa fechando o banco de dados
        print('Desconectando banco de dados')

    # Montand as tabelas do banco de ddos
    def monta_tabelas(self):  # função de montar tabelas
        self.conecta_bd()  # função vai conectar o banco de dados, PRECITO TER ESSA FUNÇÃO PARA QUANDO EU PEDIR AS TABELAS ELE ENTRA NO BD

        # CRIANDO BANCO DE DADOS E DENTRO DELE AS TABELAS
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS clientes(
                cod INTEGER  PRIMARY KEY,
                nome_cliente CHAR(48) NOT NULL,
                telefone INTEGER(28),
                cidade CHAR(48)
            );
        """)
        self.conn.commit()
        print('Banco de dados criado')  # Validando o banco de dados no sistema
        self.desconecta_bd()  # desconectando o banco de dados

    def add_cliente(self):  # Função de insert ou  add dados atraves de variaveis nas entrys
        self.codigo = self.codigo_entry.get()  # vai ser auto increment
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.conecta_bd()
        # INSERINDO DADOS LEMBRANDO QUE PRECISAM SER NA MESMA ORDEM E MESMO NUMERO DE COLUNAS
        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        # apos add o cliente, ela vai limpar a lista com ela estiver e refazer select
        self.select_lista()
        self.limpa_tela()  # vai limpar as entrys para novos dados

    def select_lista(self):
        # listaCli esta dentro da lista_frame2
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()  # CHAMANDO A FUNÇÃO DE CONEXÃO DO BANCO
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)  # VARIAVE INTERNA DA FUNÇÃO select_lista()
        for i in lista:  # aqui vou fazer a extração de dados
            # inserindo os valores na tabela pela lista
            # lança dentro da treeviwel em ordem.
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

# CUIDADO COM A ORDEM DE CHAMAMENTO DAS FUNÇÕES
# nesat classe estou criando um loop para poder rodar a janela

# CONFORME VOU CRIANDO AS FUNÇÕES VOU ACRESCENDO AQUI E EM ORDEM


class Application(funcs):  # ESTOU INSERINDO A 'funcs' PARA CARREGAR AS FUNÇÃO  limpa_tela
    def __init__(self):  # defindo uma função de inicializazão da tela
        self.root = root  # minha janela esta fora da clase crio equivalencia
        self.tela()  # preciso chmar a função  senao nao abre a janela
        self.frames_de_tela()  # chamando a função dos frames de tela
        self.widgets_frame1()  # chamando a função criar botão
        self.lista_frame2()  # chamando a função do frame 2
        self.monta_tabelas()  # chamando a função de montar tabelas dentro do banco
        self.select_lista()  # ao abrir o sistema atualiza a lista com base no cadastro bd
        root.mainloop()  # FECHANDO OS COMANDOS DENTRO DA JANELA.

# TERCEIRO PASSO -  criando as configuração da tela onde vou alocar meus widgets*********************************************
    def tela(self):  # função cria tela principal de fundo base dos frames.
        # é o que vai aparecer na aba da tela
        self.root.title('Cadastro de clientes')
        self.root.configure(background='#1e3743')  # dando cor ao fundo da tela
        # dando tamanho original pra minha tela
        self.root.geometry('700x500')
        # permitindo que seja alteravel o tamanho pelo usuario
        # Posso aumentar manualemte a tela NA COMPRIMENTO POR ALTURA
        self.root.resizable(True, True)
        # tamanho maximo para aumentar
        self.root.maxsize(width=900, height=700)  # COMPRIMENTO POR ALTURA
        # tamanho minimo para diminuir
        self.root.minsize(width=500, height=400)  # COMPRIMENTO POR ALTURA

# QUARTO PASSO - CRIANDO FRAMES, OU SEJA JANELAS DENTRO DA JANELA PRINCIPAL QUE  SEPARA OS ITENS DA NOSSA TELA****************************
    # bd é largura da borda, bg é cor da borda,  dai cor da borda e largura da cor,
    def frames_de_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)  # <= largura da cor
        # usando o relative eu torno a janela responsiva de acordo com que eu aumento ou diminuo
        # aceita numeração de 0-1 onde zero é o começo e 1 o fim zero a esquerda e 1 a direita
        # relwidth ocupa a parcetagem da largura e o relheigth ocupa a altura da tela
        # DISTANCIA EM RELAÇÃO AS BORDAS DA ROOT(TELA PRINCICPAL) E/D
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96,
                           relheight=0.46)  # 0.50 % distancia EM RELAÇÃO A BORDAS ROOT(TELA PRINCIPAL) SUPERIR

    # QUARTO PASSO_2 OU SEJA - ITENS QUE SERÃO CRIADOS DENTRO DA FRAME1.*****************************
    def widgets_frame1(self):
        # Criação do botão limpar
        # Vamas definir como vai ficar o botão e a fonte dele
        # bd = borda do botão; bg é cor fundo da widget(botao, label ou Entry) do botão,
        # fg é a cor do texto , fonte com tres valores(nome da fonte, tamanho e formatação)
        self.btn_limpar = Button(self.frame_1, text='Limpar', bd=2,
                                 bg='#187db2', fg='white', font=('Verdana', 8, 'bold'),
                                 command=self.limpa_tela)  # lembra dizer que posso usar a funcs no application
        self.btn_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação do botão Buscar
        self.btn_buscar = Button(self.frame_1, text='Buscar', bd=2,
                                 bg='#187db2', fg='white', font=('Verdana', 8, 'bold'))
        self.btn_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação do botão Novo
        self.btn_novo = Button(self.frame_1, text='Novo', bd=2,
                               bg='#187db2', fg='white', font=('Verdana', 8, 'bold'), command=self.add_cliente)  # NAO ESQUECER DE ADD O COMMAND.
        self.btn_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação do botão Alterar
        self.btn_alterar = Button(self.frame_1, text='Alterar', bd=2,
                                  bg='#187db2', fg='white', font=('Verdana', 8, 'bold'))
        self.btn_alterar.place(
            relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação do botão Apagar
        self.btn_apagar = Button(self.frame_1, text='Apagar', bd=2,
                                 bg='#187db2', fg='white', font=('Verdana', 8, 'bold'))
        self.btn_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação da Label Entrada de códigos
        # Alterando a cor de fundo das labels para #dfe3ee essa cor é a mesma da bg frame 1
        # Pondo a mesa cor das letras da mesma cor do fundo dos botões
        # LEMBRANDO QUE EU POSSO ALTERAR CORES DE FUNDO E OUTRAS NAS ENTRYs
        self.lb_codigo = Label(self.frame_1, text='Codigo', font=(
            'Verdana', 10), bg='#dfe3ee', fg='#187db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.09)

        # Criação da Labele Entrada de Nome
        self.lb_nome = Label(self.frame_1, text='Nome', font=(
            'Verdana', 10),
            bg='#dfe3ee', fg='#187db2')
        # mesmo distancia e mais baixo
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)  # linha por altura
        self.nome_entry.place(relx=0.05, rely=0.45,
                              relwidth=0.8)  # 80% do campo

        # Criação da Labele Entrada de Telefone
        self.lb_fone = Label(self.frame_1, text='Telefone', font=(
            'Verdana', 10),
            bg='#dfe3ee', fg='#187db2')
        # 60% mesmo distancia e mais baixo
        self.lb_fone.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.frame_1)  # linha por altura
        self.fone_entry.place(relx=0.05, rely=0.7,
                              relwidth=0.3)  # 30% do campo

        # Criação da Labele Entrada de Cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade', font=(
            'Verdana', 10),
            bg='#dfe3ee', fg='#187db2')
        # 60% mesmo distancia e mais baixo
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)  # linha por altura
        self.cidade_entry.place(relx=0.5, rely=0.7,
                                relwidth=0.35)  # 35% do campo

# CRIANDO FUNÇÕES ENTRO DO FRAME 2 QUE É A PARTE DE BAIXO DA TELA DOS NOSS SISTEMA

    def lista_frame2(self):
        # A Treeview tem que ser informada onde ela vai estar, qual o frame ela pertence
        # Com o comando height vemos que ele vai estar abaixo dentro da janela
        self.listaCli = ttk.Treeview(self.frame_2, height=3,
                                     column=('col1', 'col2', 'col3', 'col4'))  # TEM QUE ESTA DENTRO DAS DECLARAÇÕES DE CLASSES
    # Preciso dai então especificar o cabeçalo de cada coluna
    # Neste ponto vai mostrar o que eu coloquei na frame 1
        self.listaCli.heading('#0', text='')  # coluna zero estara vazia,
        self.listaCli.heading('#1', text='Código')  # coluna do código
        self.listaCli.heading('#2', text='Nome')  # coluna do nome do cliente
        self.listaCli.heading('#3', text='Telefone')  # coluna  numero telefone
        self.listaCli.heading('#4', text='Cidade')  # coluna  cidade  cliente

    # Especificando o tamanho de cada coluna
        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

# Ordenando posicionamento das colunas
# 0.01 començando a 1% do lado esquerdo para a direita
# 0.1  1% de cima para baixo
# 0.95 relwidth largura de 95%
# 0.95 relhwight altura de 95%
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)


# CRIANDO BARRA DE ROLAGEM
# Criando uma varialve que vai receber a função Scrollbar
# Que pertence ao Frame2 e sua orientação é vertical
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        # Informando ao tkinter que essa barra de rolagem pertence a listaCli
        self.listaCli.configure(yscroll=self.scroolLista.set)
        # Informando a posição onde vai ficar a barra de rolagem
        # relx = onde 0.01 começou da esquerda pra direita enta é 0.96 + 0.01 = 0.97
        # rely mantem por conta da altura
        # relhidth é a sobre da largura de 100% ou seja me sobra 0.04%
        # relheight é a altura da barra de rolagem em relação ao  espaçamento dos 0.85
        self.scroolLista.place(relx=0.96, rely=0.1,
                               relwidth=0.04, relheight=0.85)


# chamando a função para mostrar a janela, encerrando assim o loop. NÃO É A MESMA COISA QUE MAINLOOP().
Application()
# parei em 1: 40 https: // www.youtube.com/watch?v=owLh_n73xXI&t=5463s
