import tkinter as tk
from tkinter import *
import tkinter.font as tk_font

janela = tk.Tk()
janela.title('Calculadora')


def inserir(valor):
    display.insert(END, valor)


def limpar():
    display.delete(0, END)


def calcular():
    texto_display = display.get()
    resultado = eval(texto_display)
    display.delete(0, END)
    display.insert(0, str(resultado))


# entrada de números
font_style = tk_font.Font(janela, family='Digital-7', size=40)
display = Entry(janela, font=font_style, bg='#FFFAFA', fg='#000000', width=11)
display.pack()

# criar o painel para inserir os botões para serem chamados
panel = Frame(janela)

# ativar painel
panel.pack()

# criar botões
botao_ce = Button(panel, bg='#D3D3D3', bd=1, text='CE', font='Arial 16 bold',
                  fg='#000000', width=5, height=2, command=lambda: limpar())
botao_c = Button(panel, bg='#D3D3D3', bd=1, text='C', font='Arial 16 bold',
                 fg='#000000', width=5, height=2, command=lambda: inserir('C'))
botao_apagar = Button(panel, bg='#D3D3D3', bd=1, text='<x|', font='Arial 16 bold',
                      fg='#000000', width=5, height=2, command=lambda: inserir('<x|'))
botao_divisao = Button(panel, bg='#D3D3D3', bd=1, text='/', font='Arial 16 bold',
                       fg='#000000', width=5, height=2, command=lambda: inserir('/'))

botao_7 = Button(panel, bg='#D3D3D3', bd=1, text='7', font='Arial 16 bold',
                 fg='#000000', width=5, height=2, command=lambda: inserir('7'))
botao_8 = Button(panel, bg='#D3D3D3', bd=1, text='8', font='Arial 16 bold',
                 fg='#000000', width=5, height=2, command=lambda: inserir('8'))
botao_9 = Button(panel, bg='#D3D3D3', bd=1, text='9', font='Arial 16 bold',
                 fg='#000000', width=5, height=2, command=lambda: inserir('9'))
botao_multiplicacao = Button(panel, bg='#D3D3D3', bd=1, text='x', font='Arial 16 bold',
                             fg='#000000', width=5, height=2, command=lambda: inserir('*'))

botao_4 = Button(panel, bg='#D3D3D3', bd=1, text='4', font='Arial 16 bold',
                 fg='#000000', width=5, height=2, command=lambda: inserir('4'))
botao_5 = Button(panel, bg='#D3D3D3', bd=1, text='5', font='Arial 16 bold',
                 fg='#000000', width=5, height=2, command=lambda: inserir('5'))
botao_6 = Button(panel, bg='#D3D3D3', bd=1, text='6', font='Arial 16 bold',
                 fg='#000000', width=5, height=2, command=lambda: inserir('6'))
botao_subtracao = Button(panel, bg='#D3D3D3', bd=1, text='-', font='Arial 16 bold',
                         fg='#000000', width=5, height=2, command=lambda: inserir('-'))

botao_1 = Button(panel, bg='#D3D3D3', bd=1, text='1', font='Arial 16 bold',
                 fg='#000000', width=5, height=2, command=lambda: inserir('1'))
botao_2 = Button(panel, bg='#D3D3D3', bd=1, text='2', font='Arial 16 bold',
                 fg='#000000', width=5, height=2, command=lambda: inserir('2'))
botao_3 = Button(panel, bg='#D3D3D3', bd=1, text='3', font='Arial 16 bold',
                 fg='#000000', width=5, height=2, command=lambda: inserir('3'))
botao_adicao = Button(panel, bg='#D3D3D3', bd=1, text='+', font='Arial 16 bold',
                      fg='#000000', width=5, height=2, command=lambda: inserir('+'))

botao_mais_menos = Button(panel, bg='#D3D3D3', bd=1, text='+/-', font='Arial 16 bold',
                          fg='#000000', width=5, height=2, command=lambda: inserir('+/-'))
botao_0 = Button(panel, bg='#D3D3D3', bd=1, text='0', font='Arial 16 bold',
                 fg='#000000', width=5, height=2, command=lambda: inserir('0'))
botao_virgula = Button(panel, bg='#D3D3D3', bd=1, text=',', font='Arial 16 bold',
                       fg='#000000', width=5, height=2, command=lambda: inserir(','))
botao_igual = Button(panel, bg='#D3D3D3', bd=1, text='=', font='Arial 16 bold',
                     fg='#000000', width=5, height=2, command=lambda: calcular())

botao_ce.grid(row=1, column=0)
botao_c.grid(row=1, column=1)
botao_apagar.grid(row=1, column=2)
botao_divisao.grid(row=1, column=3)

botao_7.grid(row=2, column=0)
botao_8.grid(row=2, column=1)
botao_9.grid(row=2, column=2)
botao_multiplicacao.grid(row=2, column=3)

botao_4.grid(row=3, column=0)
botao_5.grid(row=3, column=1)
botao_6.grid(row=3, column=2)
botao_subtracao.grid(row=3, column=3)

botao_1.grid(row=4, column=0)
botao_2.grid(row=4, column=1)
botao_3.grid(row=4, column=2)
botao_adicao.grid(row=4, column=3)

botao_mais_menos.grid(row=5, column=0)
botao_0.grid(row=5, column=1)
botao_virgula.grid(row=5, column=2)
botao_igual.grid(row=5, column=3)

mainloop()
