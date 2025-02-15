# import pyautogui
# import pyautogui as escolha_opcao

# opcao = pyautogui.confirm('Clique no botão desejado', buttons= ['Notepad', 'Discord',])
# if opcao == "Notepad":
#     escolha_opcao.hotkey('win', 'r')
#     escolha_opcao.sleep(2)
#     escolha_opcao.typewrite('Notepad')
#     escolha_opcao.press('enter')
# elif opcao == "Discord":
#     escolha_opcao.hotkey('win', 'r')
#     escolha_opcao.sleep(2)
#     escolha_opcao.typewrite("C:\\Users\\Joden\\AppData\\Local\\Discord\\app-1.0.9182\\Discord.exe")
#     escolha_opcao.press('enter')

import tkinter as tk
from tkinter import messagebox
import pyautogui as escolha_opcao

def abrir_programa(opcao):
    if opcao == "Notepad":
        escolha_opcao.hotkey('win', 'r')
        escolha_opcao.sleep(2)
        escolha_opcao.typewrite('Notepad')
        escolha_opcao.press('enter')
    elif opcao == "Discord":
        escolha_opcao.hotkey('win', 'r')
        escolha_opcao.sleep(2)
        escolha_opcao.typewrite("C:\\Users\\Joden\\AppData\\Local\\Discord\\app-1.0.9182\\Discord.exe")
        escolha_opcao.press('enter')

def escolher_opcao():
    root = tk.Tk()
    root.title("Escolha um Programa")
    root.geometry("300x150")
    root.configure(bg="#1e1e1e")  # Cor de fundo preta

    label = tk.Label(root, text="Selecione um programa:", font=("Arial", 12, "bold"), fg="lime", bg="#1e1e1e")
    label.pack(pady=10)

    btn_notepad = tk.Button(root, text="Notepad", font=("Arial", 10, "bold"), fg="#8b0000", bg="blue", command=lambda: [abrir_programa("Notepad"), root.destroy()])
    btn_notepad.pack(pady=5)

    btn_discord = tk.Button(root, text="Discord", font=("Arial", 10, "bold"), fg="#8b0000", bg="green", command=lambda: [abrir_programa("Discord"), root.destroy()])
    btn_discord.pack(pady=5)

    root.mainloop()

# Chama o menu personalizado
escolher_opcao()
