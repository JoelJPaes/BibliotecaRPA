# Exercício: Calculadora Simples
# Desenvolva uma calculadora simples que permite ao usuário realizar operações 
# básicas de adição, subtração, multiplicação e divisão.
# Objetivos:
#     Mostrar um Menu ao Usuário:
#         - A calculadora deve exibir um menu com cinco opções: 
#             - adição
#             - subtração
#             - multiplicação
#             - divisão
#             - sair
#         O usuário deve ser capaz de selecionar a operação desejada através da entrada de um número correspondente.
#     Receber Dois Números:
#         - Após selecionar a operação, o usuário deve inserir dois números
#         que serão utilizados na operação.
#     Realizar a Operação Selecionada:
#         - A calculadora deve realizar a operação selecionada com os números 
#         inseridos e exibir o resultado.
#     Repetir ou Encerrar:
#         - Após cada operação, o menu deve ser exibido novamente, permitindo que 
#         o usuário realize outra operação ou saia do programa.
#         - O programa deve continuar funcionando até que o usuário escolha sair.
# Boa sorte e divirta-se programando!

while True:
    print("\nCalculadora Simples")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = input("Escolha uma opção (1-5): ")
    if opcao == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print("Resultado:", resultado)
    elif opcao == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print("Resultado:", resultado)
    elif opcao == "3":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print("Resultado:", resultado)
    elif opcao == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Erro: Divisão por zero não é permitida.")
    elif opcao == "5":
        print("Saindo da calculadora.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")