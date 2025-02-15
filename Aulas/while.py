# numero = 1
# max = input("Digite um inteiro maior que 1: ")
# print("Números pares entre 1 e", max, ":")
# while numero <= max:
#     if numero % 2 == 0:
#         print(numero)
#     numero += 1

# Exercício:

# Crie um algoritmo que solicite ao usuário 
# uma senha, e só sai do
# # looping do While quando for 
# digitado a senha corretamente

# senha = 18071995
# senha_digitada = int(input("Digite a senha: "))
# while senha_digitada != senha:#se a senha digitada for diferente da senha
#     print("Senha incorreta. Tente novamente.")
#     senha_digitada = int(input("Digite a senha: "))
# print("Senha correta. Acesso permitido.")

# Exercício:

# Crie um algoritmo que leia  números inteiros digitados pelo usuário,
# e só pare quando o usuário digite 0.

# No final, imprima,na tela a soma de todos os números digitados.


# somaNumerosDigitados = 0
# numero =int(input("Digite um número inteiro (ou 0 para sair): "))
# while numero != 0:
#     somaNumerosDigitados += (numero)
#     numero =int(input("Digite um número inteiro (ou 0 para sair): "))
# print("Total:", somaNumerosDigitados)


# Exercício:
# Crie um algoritmo que leia numeros inteiros positivos 
# digitados pelo usuario
# até que o usuário digite um número menor que 0. No final, 
# imprima o maior número digitado.

# maiornumero = -1
# NumeroDigitado = int(input("Digite um número inteiro e maior que zero: "))
# while NumeroDigitado >= 0:
#     if NumeroDigitado > maiornumero:
#         maiornumero = NumeroDigitado
#     NumeroDigitado = int(input("Digite um número inteiro e maior que zero: "))
# print("O maior número digitado foi:", maiornumero)