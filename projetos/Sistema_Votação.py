import tkinter as tk
from tkinter import messagebox

def clique_botao(valor):
    print(f"Botão {valor} pressionado")
    if valor == "B":
        messagebox.showinfo("Voto", "Voto em BRANCO registrado!")
    elif valor == "N":
        messagebox.showinfo("Voto", "Voto NULO registrado!")
    else:
        messagebox.showinfo("Voto", f"Voto no CANDIDATO {valor} registrado!")

app = tk.Tk()
app.title("Sistema de Votação")
app.geometry("300x350")
app.configure(padx=20, pady=20)

# Configurando o peso das colunas para centralizar os botões
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

# Título ou instruções
label_titulo = tk.Label(app, text="Digite seu voto:", font=("Arial", 14, "bold"))
label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Criando os botões com um layout de grade (grid)
botoes = [
    ("Candidato 1", "1", 1, 0),
    ("Candidato 2", "2", 1, 1),
    ("Branco", "B", 2, 0),
    ("Nulo", "N", 2, 1)
]

for texto, valor, linha, coluna in botoes:
    # Se o botão for Candidato 1 ou 2, usa a cor padrão; caso contrário, muda a cor
    cor_fundo = "lightgray" if valor in ["1", "2"] else "white"
    
    botao = tk.Button(
        app, 
        text=texto, 
        font=("Arial", 12),
        width=12,
        height=2,
        bg=cor_fundo,
        command=lambda v=valor: clique_botao(v)
    )
    botao.grid(row=linha, column=coluna, padx=10, pady=10)

app.mainloop()
