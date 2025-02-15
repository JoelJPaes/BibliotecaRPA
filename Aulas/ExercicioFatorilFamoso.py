# Exercício

# Crie um programa em Python que solicite ao usuário que digite um número inteiro
# não negativo. Em seguida, calcule e exiba o fatorial desse número.

# Digite um número inteiro não negativo: 5
# O fatorial de 5 é: 120
# """

# # Solicita ao usuário a entrada de um número inteiro não negativo

Numero = int(input("Digite um número inteiro não negativo: "))
# Inicializa a variável para armazenar o fatorial
Fatorial = 1
# Verifica se o número é negativo
if Numero < 0:
    print("O número deve ser não negativo.")
else:
    Fatorial = 1
    for i in range(1, Numero + 1):
        Fatorial *= i
    print(f"O fatorial de {Numero} é: {Fatorial}")
    