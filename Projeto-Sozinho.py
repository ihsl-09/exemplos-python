import tkinter as tk

janela = tk.Tk()
janela.title("Não tem nada aqui")
janela.geometry("500x300")
tk.Label(janela, text=f"Bem Vinda").pack()
texto = tk.Label(janela, text=f"")
texto.pack()
def resposta_botao():
    nome = entrada_name.get()
    texto['text'] = f"Ola {nome}"

entrada_name = tk.Entry(janela)
entrada_name.pack()
tk.Button(janela, text="Botão da alegria", command=resposta_botao).pack()



janela.mainloop()