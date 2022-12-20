from tkinter import *
from tkinter import Menu
import tkinter as tk


def salvar():
    text = barra_texto.get(1.0, END)
    with open('arquivo.txt', 'w') as file:
        file.write(text)
        barra_texto.delete(1.0, END)
        print('Arquivo salvo com sucesso!')


def abrir():
    with open('arquivo.txt', 'r') as file:
        text = file.read()
        barra_texto.insert(1.0, text)


bloco = tk.Tk()
bloco.title('Bloco de Notas')
bloco.geometry('600x400')

barra = Frame(bloco, height=30, bg='#DCDCDC', bd=0)
barra.pack()

barra_texto = Text(bloco, font='Lucida 14')
barra_texto.pack(expand=True, fill='both')

barra_menu = Menu(bloco, title='Arquivo')
bloco.config(menu=barra_menu)
menu_arquivo = Menu(barra_menu)
barra_menu.add_cascade(label='Arquivo', menu=menu_arquivo)
menu_arquivo.add_command(label='Abrir', command=abrir)
menu_arquivo.add_command(label='Salvar', command=salvar)
menu_arquivo.add_command(label='Configurações')
menu_arquivo.add_command(label='Sair', command=bloco.quit)

display = Text(bloco, font='Arial', bg='#FFFAFA', fg='#000000')
display.pack()

bloco.mainloop()
