import tkinter as tk
from tkinter import *

janela_cadastro = tk.Tk()
janela_cadastro.title('Tela de cadastro')

Label(janela_cadastro, text='CADASTRO').grid(row=0, sticky=W)
Label(janela_cadastro, text='Nome:').grid(row=1, sticky=W)
Label(janela_cadastro, text='Senha:').grid(row=2, sticky=W)
Label(janela_cadastro, text='Escolha do curso').grid(row=3, sticky=W)

entrada_nome = Entry(janela_cadastro)
entrada_senha = Entry(janela_cadastro, show='*')

entrada_nome.grid(row=1, column=1)
entrada_senha.grid(row=2, column=1)

Radiobutton(janela_cadastro, text='Programação', value=1).grid(row=4, sticky=W)
Radiobutton(janela_cadastro, text='Criativo', value=2).grid(row=5, sticky=W)
Radiobutton(janela_cadastro, text='Fotografia', value=3).grid(row=6, sticky=W)

Button(janela_cadastro, text='ENTRAR', width=15).grid(row=7, column=0)
Button(janela_cadastro, text='FECHAR', width=15).grid(row=7, column=1)
mainloop()
