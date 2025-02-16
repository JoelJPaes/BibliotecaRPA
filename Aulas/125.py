import tkinter as tk
import time
import os
import pyautogui as escolha_opcao
import pyperclip
from tkinter import messagebox

def digitar_texto(texto):
    """Função que digita corretamente os caracteres acentuados com um pequeno atraso."""
    pyperclip.copy(texto)  # Copia o texto para a área de transferência
    escolha_opcao.hotkey("ctrl", "v")  # Cola o texto
    time.sleep(0.5)  # Dá tempo para o texto ser inserido corretamente

def abrir_programa(opcao):
    if opcao == "Notepad":
        escolha_opcao.hotkey('win', 'r')  # Abre o Executar
        time.sleep(2)
        escolha_opcao.typewrite('Notepad', interval=0.1)
        escolha_opcao.press('enter')

        time.sleep(4)  # Aguarda o Notepad abrir completamente

        texto = "o bocanejo é um trupaneto com mara de buscopan"
        digitar_texto(texto)  # Usa a função personalizada para garantir os acentos

    elif opcao == "Discord":
        caminho_discord = "C:\\Users\\Joden\\AppData\\Local\\Discord\\app-1.0.9182\\Discord.exe"
        
        if os.path.exists(caminho_discord):  # Verifica se o caminho do Discord existe
            escolha_opcao.hotkey('win', 'r')
            time.sleep(2)
            escolha_opcao.typewrite(caminho_discord, interval=0.05)
            escolha_opcao.press('enter')
        else:
            messagebox.showerror("Erro", "O caminho do Discord não foi encontrado!")

def escolher_opcao():
    root = tk.Tk()
    root.title("Escolha um Programa")
    root.geometry("300x180")
    root.configure(bg="#1e1e1e")  # Cor de fundo preta

    label = tk.Label(root, text="Selecione um programa:", font=("Arial", 12, "bold"), fg="lime", bg="#1e1e1e")
    label.pack(pady=10)

    btn_notepad = tk.Button(root, text="Abrir Notepad", font=("Arial", 10, "bold"), fg="white", bg="blue",
                            width=20, command=lambda: [abrir_programa("Notepad"), root.destroy()])
    btn_notepad.pack(pady=5)

    btn_discord = tk.Button(root, text="Abrir Discord", font=("Arial", 10, "bold"), fg="white", bg="green",
                            width=20, command=lambda: [abrir_programa("Discord"), root.destroy()])
    btn_discord.pack(pady=5)

    btn_sair = tk.Button(root, text="Fechar", font=("Arial", 10, "bold"), fg="white", bg="red",
                         width=20, command=root.destroy)
    btn_sair.pack(pady=10)

    root.mainloop()

# Chama o menu personalizado
escolher_opcao()
