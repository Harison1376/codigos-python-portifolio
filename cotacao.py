
import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes['text'] = texto


root = Tk()
root.title('Cotação moedas')
root.geometry('300x200')
root.resizable(True, True)
root.maxsize(width=350, height=230)
root.minsize(width=290, height=150)

texto_orientacao = Label(
    root, text='Click no botão para saber a cotação da moeda')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(root, text='Buscar cotações dólar, Euro, BTC',
               command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(root, text='')
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

root.mainloop()  # Finaliza o código mais nao fecha a janela
