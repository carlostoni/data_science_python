import tkinter as tk
from tkinter import ttk


def soma():
    n1 = float(input_entry.get())
    n2 = float(input_entry2.get())
    soma= n1 + n2
    label_resultado.config(text=soma)


janela = tk.Tk()
janela.geometry('500x500')
janela.title("RESTANDO TKINTER")

text_label = tk.Label(janela, text='isso e um texto')
text_label.pack()

input_entry =  tk.Entry(janela)
input_entry.pack()


input_entry2 =  tk.Entry(janela)
input_entry2.pack()


botao = tk.Button(janela, text = 'clique aqui', command= soma)
botao.pack()

label_resultado = tk.Label(janela, text='Resultado ')
label_resultado.pack()


janela.mainloop()