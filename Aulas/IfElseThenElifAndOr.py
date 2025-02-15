
# numero1 = 12
# numero2 = 12


# if numero1 > numero2:

#     print("O número 1 é maior que o número 2")

# elif numero1 == numero2:

#     print("Os números são iguais")

# Execute o programa.
# Insira um número inteiro entre 1 e 10 quando solicitado.
# O programa irá informar se você adivinhou corretamente o número secreto ou não.

# Seu objetivo é descobrir qual é o número secreto. Você pode executar o programa
# quantas vezes quiser ate adivinhar corretamente.

# Nota: Para fins deste exercício, o número secreto é fixo e é igual a 7. Em uma
# versão mais avançada do exercício, você poderia modificar o programa para escolher um
# secreto aleatório cada vez que é executado.
#comente cada linhaa do código


# número_secreto = 7

# chute = int(input("Digite um número entre 1 e 10: ")) #input é uma função que recebe um valor do usuário
# if chute == número_secreto:#se o chute for igual ao número secreto
#     print("Você acertou!")#se o chute for igual ao número secreto
# else:#se o chute não for igual ao número secreto
#     print("Você errou!")#se o chute não for igual ao número secreto
#     # Execute o programa.

# Exercício:

# Verifique a Elegibilidade para Votar

# Neste exercício, você vai executar um programa que determina
# se uma pessoa está ou não elegível para votar com base em sua idade.

# Execute o programa.
# Insira sua idade quando solicitado.
# O programa irá informar se você é elegível para votar ou não.

# Note que a idade mínima para votar é de 18 anos.

# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é elegível para votar!")
# else:
#     print("Você não é elegível para votar.")

# nota = 60#nota de 0 a 100

# if nota >= 90:#se a nota for maior ou igual a 90
#     print("Aprovado com excelência! 🎉")
# elif nota >= 60:#se a nota for maior ou igual a 60
#     print("Aprovado! ✅")
# elif nota >= 50:#se a nota for maior ou igual a 50
#     print("Recuperação. 📚")
# else:#se a nota for menor que 60
#     print("Reprovado. ❌")#se a nota for menor que 60

# Exercício:

# Classificacao de Notas

# Neste exercício, seu objetivo é executar um programa que
# classifica as notas de um estudante em diferentes categorias.

# Execute o programa.

# Insira a nota do estudante quando solicitado (entre 0 e 100).

# O programa irá informar a classificação da nota de acordo com os seguintes critérios:
# Excelente: 90-100
# Bom: 70-89
# Satisfatório: 50-69
# Insuficiente: 0-49

# Excelente: 90-100
# Bom: 70-89
# Satisfatório: 50-69
# Insuficiente: 0-49
# nota = int(input("Digite a nota do estudante: "))
# if nota >= 90 and nota <= 100:#se a nota for maior ou igual a 90 e menor ou igual a 100
#     print("Excelente! 🎉")

# elif nota >= 70 and nota <= 89:#se a nota for maior ou igual a 70 e menor ou igual a 89
#     print("Bom! ✅")

# elif nota >= 50 and nota <= 69:#se a nota for maior ou igual a 50 e menor ou igual a 69
#     print("Satisfatório. 📚")

# elif nota >= 0 and nota <= 49:#se a nota for maior ou igual a 0 e menor ou igual a 49
#     print("Insuficiente. ❌")

# else:#se a nota for menor que 0 ou maior que 100
#     print("Nota inválida. Digite um número entre 0 e 100.")

# Exercicio:

# Calculadora de Descontos

# Você é um cliente em uma loja que está tendo uma promoção especial. Dependendo
# do valor da sua compra, voce pode receber um desconto!

# Execute o programa.
# Insira o valor da sua compra quando solicitado.
# O programa ira calcular e informar o valor do desconto aplicado e o valor final
# com o desconto.

# Os descontos são aplicados da seguinte forma:

# Compras acima de R$1000 recebem 20% de desconto.
# Compras de $500 a R$1000 recebem 10% de desconto.
# Compras abaixo de R$500 nao recebem desconto.

# valor_compra = float(input("Digite o valor da compra: "))

# if valor_compra > 1000:
#     desconto = valor_compra * 0.2
#     print("Você recebeu um desconto de 20%!")
# elif valor_compra >= 500 and valor_compra <= 1000:
#     desconto = valor_compra * 0.1
#     print("Você recebeu um desconto de 10%!")


# else:
#     desconto = 0
#     print("Você não recebeu desconto.")
#     print("Obrigado por comprar conosco!")
#     print("Volte sempre!")
#     print("Até logo!")


# valor_final = valor_compra - desconto
# print(f"Valor do desconto: R$ {desconto:.2f}")
# print(f"Valor final da compra: R$ {valor_final:.2f}")

# Exercício

# Entrada para um Evento Exclusivo

# Você foi convidado para um evento exclusivo. Para entrar, você deve
# atender a pelo menos uma das seguintes condições:

# Ter um convite VIP.
# Estar na lista de convidados.
# Ser um membro do clube.

# Execute o programa.

# Responda às perguntas fornecidas com 'sim' ou 'não'.
# O programa irá informar se você pode entrar no evento ou não.

# Bem-vindo(a) ao evento!
# Desculpe, você nao pode entrar no evento.

# condicao1 = False
# condicao2 = False
# condicao3 = False

# if condicao1 or condicao2 or condicao3:
#     print("Bem-vindo(a) ao evento!")

# else:
#     print("Desculpe, você não pode entrar no evento.")
#     print("Volte sempre!")
#     print("Até logo!")

# convite_vip = input("Você tem um convite VIP? (sim/não): ")
# na_lista = input("Você está na lista de convidados? (sim/não): ")
# membro_clube = input("Você é membro do clube? (sim/não): ")

# if convite_vip == "sim" or na_lista == "sim" or membro_clube == "sim":
#     print("Bem-vindo(a) ao evento!")

# else:


#Exercicio Par ou Impar
#Crie um algoritmo que solicite a entrada de um número positivo e inteiro e imprima se o
#número é PAR ou IMPAR
# numero = 45
# resultado = "par" if numero % 2 == 0 else "impar"#se o numero for par, o resultado sera par, se nao, sera impar
# print(resultado)

