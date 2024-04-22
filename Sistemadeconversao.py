from tkinter import *
import tkinter as tk
import re

# Função para converter centímetros em metros
def calculo():
    # Obtém o valor inserido pelo usuário
    cm = dados.get()
    
    # Verifica se o valor inserido é um número válido
    if re.match(r'^\d*[\.,]?\d*$', cm):
        # Converte ',' para '.' se houver
        cm = float(cm.replace(',', '.'))
        # Converte centímetros para metros
        m = cm / 100
        # Exibe o resultado
        l_result.config(text=f'{cm} Centímetros equivalem a {m} metros.')
    else:
        # Exibe uma mensagem de erro se o valor inserido não for válido
        l_result.config(text='Por favor, Insira um valor válido.')

# Cria a janela principal
root = Tk()
root.title('Conversão de centímetros para metros')
root.geometry('450x300')

# Label e Entry para o valor em centímetros
mensagem_cm = tk.Label(root, text='Digite o número que deseja converter:', font=('Georgia', 9, 'bold'))
mensagem_cm.grid(row=0, column=0)

dados = tk.Entry(root)
dados.grid(row=0, column=1)

# Botão para realizar a conversão
btn = tk.Button(root, text='Converter', command=calculo)
btn.grid(row=1, column=1)

# Label para exibir o resultado
l_result = tk.Label(root, text="", font=('Georgia', 9, 'bold'))
l_result.grid(row=3, column=0, columnspan=2)

# Inicia o loop principal da aplicação
root.mainloop()
