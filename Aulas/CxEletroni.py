# Exercicio: Simulação de Caixa Eletrônico
# Objetivo: Desenvolver um programa em Python que simula as
# operacoes basicas de um caixa eletronico. O usuario deve ser capaz de
# verificar o saldo, depositar dinheiro, sacar dinheiro e sair do programa.
# Requisitos:
# Verificar Saldo:
# - Ao escolher essa opcao, o programa deve exibir o saldo atual da conta.
# Depositar Dinheiro:
# - O usuário deve ser capaz de inserir uma quantia para depositar na conta.
# - A quantia deve ser positiva.
# - Após um depósito bem-sucedido, o saldo da conta deve ser atualizado e uma
# mensagem de confirmação deve ser exibida.
# Sacar Dinheiro:
# - O usuario deve ser capaz de inserir uma quantia para sacar da conta.
# - A quantia deve ser positiva e não deve exceder o saldo atual.
# - Após um saque bem-sucedido, o saldo da conta deve ser
# atualizado e uma mensagem de confirmacao deve ser exibida.
# Sair:
# - O usuário deve ser capaz de sair do programa escolhendo essa opçao.
# Validação de Entrada:
# - O programa deve lidar com entradas inválidas de forma adequada, exibindo mensagens de erro quando aplicável.
# Interface de Usuário:
# - O programa deve exibir um menu de opções para o usuário e permitir
# a seleção de ações a serem realizadas.
# - As opções do menu devem ser apresentadas em um loop, permitindo
# múltiplas operações até que o usuário escolha sair.
# Caixa Eletrônico
# 1 - Verificar Saldo
# 2 - Depositar Dinheiro
# 3 - Sacar Dinheiro
# 4 - Sair
# Escolha uma opção (1-4):
# 00:05:02 1o
# Saldo Inicial:
# - A conta deve começar com um saldo inicial de R$ 1000.00.
# Instruções:
# - Comece inicializando o saldo e entrando em um loop que apresente o menu de opções.
# - Implemente cada operação como descrito nos requisitos.
# - Certifique-se de testar todas as opções e cenários possíveis para garantir que
# o programa funcione corretamente.
# Dica: Você pode usar condicionais if, elif, e else juntamente com um loop while
# para gerenciar as seleções do usuário e manter o programa em execução
# até que a opção de sair seja escolhida.

saldo = 1000.0

while True:
    print("\nCaixa Eletrônico")
    print("1 - Verificar Saldo")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Sair")
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "2":
        deposito = float(input("Digite a quantia para depositar: "))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
        else:
            print("A quantia deve ser positiva.")
    elif opcao == "3":
        saque = float(input("Digite a quantia para sacar: "))
        if 0 < saque <= saldo:
            saldo -= saque
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou quantia inválida.")
    elif opcao == "4":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")