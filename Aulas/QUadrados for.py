# Exercício: Soma dos Quadrados

# Objetivo: Escreva um programa que peça ao usuário um número inteiro positivo NN e 
# calcule a soma dos quadrados de todos os números inteiros de 1 até NN. Utilize um loop 
# for para esta tarefa.

# Etapas:

#     - Solicite ao usuário um número inteiro positivo NN.
    
#     - Utilize um loop for para iterar de 1 a NN, calculando o quadrado 
#     de cada número e somando-o a uma variável.
    
#     - Imprima o resultado da soma.

# Exemplo de Saída:

# Digite um número inteiro positivo: 5
# Quadrado de 1: 1
# Quadrado de 2: 4
# Quadrado de 3: 9
# Quadrado de 4: 16
# Quadrado de 5: 25
# A soma dos quadrados dos números de 1 até 5 é: 55

N = int(input("Digite um número inteiro positivo: "))
soma_quadrados = 0
for i in range(1, N + 1):
    quadrado = i ** 2
    soma_quadrados += quadrado
    print(f"Quadrado de {i}: {quadrado}")
print(f"A soma dos quadrados dos números de 1 até {N} é: {soma_quadrados}")