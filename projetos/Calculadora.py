import tkinter as tk
from tkinter import messagebox

# --- Funções de Lógica ---
def clique_botao(valor):
    """Atualiza o visor quando um botão é pressionado."""
    atual = visor.get()
    visor.delete(0, tk.END)
    visor.insert(0, str(atual) + str(valor))

def limpar_visor():
    """Limpa o visor da calculadora."""
    visor.delete(0, tk.END)

def calcular():
    """Avalia a expressão no visor."""
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", "Expressão Inválida")
        limpar_visor()

# --- Configuração da Interface (GUI) ---
app = tk.Tk()
app.title("Calculadora Simples")
app.geometry("300x400")
app.resizable(False, False) # Impede redimensionar

# Visor
visor = tk.Entry(app, font=("Arial", 20), justify="right", bd=10)
visor.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Definição dos botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Criar e posicionar botões usando grid
linha = 1
coluna = 0

for botao in botoes:
    # Define o comando baseado no texto do botão
    if botao == '=':
        comando = calcular
    elif botao == 'C':
        comando = limpar_visor
    else:
        # Usa lambda para passar o valor específico do botão
        comando = lambda x=botao: clique_botao(x)
    
    tk.Button(app, text=botao, font=("Arial", 14), command=comando, height=2, width=5).grid(row=linha, column=coluna, padx=2, pady=2)
    
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Ajustar pesos das linhas/colunas para expansão
for i in range(5):
    app.grid_rowconfigure(i, weight=1)
for i in range(4):
    app.grid_columnconfigure(i, weight=1)

app.mainloop()
