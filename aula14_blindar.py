from tkinter import *
import tkinter as tk

janela_principal = tk.Tk()
janela_principal.title('BIND')
janela_principal.geometry('600x400')


# criar as funções
def scroll(event):
    print(f'Rolagem pressionado em: x={event.x} y={event.y}')


def button_right_click(event):
    print(f'Botão Direito pressionado em: x={event.x} y={event.y}')


def double_click(event):
    print(f'Duplo clique em pressionado em: x={event.x} y={event.y}')


frame = Frame(janela_principal, height=400, width=600)

# criar botões
frame.bind('<Double 1>', double_click)
frame.bind('<Button-2>', scroll)
frame.bind('<Button-3>', button_right_click)

frame.pack()
mainloop()
