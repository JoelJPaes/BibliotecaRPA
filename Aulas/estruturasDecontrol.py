import time

def login():
    usuarios = {"joel": "1234", "admin": "admin"}
    tentativas = 3
    
    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        
        if usuario in usuarios and usuarios[usuario] == senha:
            print("Login bem-sucedido!\n")
            return True
        else:
            tentativas -= 1
            print(f"Login falhou! Tentativas restantes: {tentativas}\n")
    
    print("Número máximo de tentativas atingido! Encerrando...")
    return False

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Contagem Progressiva")
        print("2. Contagem Regressiva")
        print("3. Mostrar Números Ímpares de 1 a 20")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            for i in range(1, 11):
                print(i, end=" ")
                time.sleep(0.5)
            print("\nContagem concluída!\n")
        
        elif escolha == "2":
            num = 10
            while num > 0:
                print(num, end=" ")
                time.sleep(0.5)
                num -= 1
            print("\nContagem concluída!\n")
        
        elif escolha == "3":
            for i in range(1, 21):
                if i % 2 == 0:
                    continue  # Pula os números pares
                print(i, end=" ")
            print("\nLista de ímpares concluída!\n")
        
        elif escolha == "4":
            print("Saindo do programa... Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.\n")

if login():
    menu()
