import pygetwindow as gw

# Pega todas as janelas abertas
windows = gw.getAllWindows()

for window in windows:
    # Verifica se a janela está visível e fecha
    if window.visible:  # Correção aqui
        window.close()
    print(f"Janela '{window.title}' fechada.")