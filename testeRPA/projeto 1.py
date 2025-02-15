# 1. Automação de Tarefas com PyAutoGUI
# Descrição: Criar um bot que automatiza tarefas no computador, como abrir e organizar pastas, mover arquivos para diretórios específicos ou abrir aplicativos automaticamente.

# Código do Projeto:

import pyautogui
import os
import time

def abrir_pasta(path):
    """Abre uma pasta específica no sistema operacional."""
    os.startfile(path)
    time.sleep(2)  # Espera 2 segundos para garantir que a pasta abriu

def mover_arquivo(origem, destino):
    """Move um arquivo de uma pasta para outra."""
    if os.path.exists(origem):
        os.rename(origem, destino)
        print(f"Arquivo movido para: {destino}")
    else:
        print("Arquivo não encontrado.")

def abrir_aplicativo(aplicativo):
    """Abre um aplicativo instalado no computador."""
    os.startfile(aplicativo)
    print(f"Abrindo {aplicativo}...")
    time.sleep(2)

# Configuração dos caminhos
pasta = "C:\\Users\\SeuUsuario\\Documents\\PastaTeste"
arquivo_origem = "C:\\Users\\SeuUsuario\\Documents\\PastaTeste\\arquivo_teste.txt"
arquivo_destino = "C:\\Users\\SeuUsuario\\Documents\\Destino\\arquivo_teste.txt"
aplicativo = "C:\\Program Files\\Notepad++\\notepad++.exe"

# Automação
print("Iniciando automação com PyAutoGUI...")
abrir_pasta(pasta)
mover_arquivo(arquivo_origem, arquivo_destino)
abrir_aplicativo(aplicativo)
print("Automação finalizada!")