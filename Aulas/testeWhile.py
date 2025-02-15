# Crie um programa em Python que peça para o 
# usuário digitar números inteiros positivos. 
# O programa deve continuar pedindo números até que o 
# usuário digite um número negativo. Quando isso acontecer, o 
# programa deve exibir a soma de todos os números positivos digitados.

# numerointeiro = int(input("Digite um número inteiro positivo: "))
soma = 0

# modo 1
# while numerointeiro >= 0:
#     soma += numerointeiro
#     numerointeiro = int(input("Digite um número inteiro positivo: "))
# print(f"A soma dos números positivos é: {soma}")

# modo 2
# while numerointeiro >= 0:
#     soma += numerointeiro
#     numerointeiro = int(input("Digite um número inteiro positivo: "))
#     if numerointeiro < 0:
#         break

#modo 3
while True:
    numerointeiro = int(input("Digite um número inteiro positivo: "))
    if numerointeiro < 0:
        print("Número negativo, encerrando o programa.")
        break
    soma += numerointeiro
print(f"A soma dos números positivos é: {soma}")