"""
Exercício: Soma de Números Pares

Objetivo: Escreva um programa que peça ao usuário um número 
inteiro N e some todos os números pares de 1 até N, incluindo o próprio N (se for par). 

Utilize um loop for para esta tarefa.

Etapas:

    - Solicite ao usuário um número inteiro positivo N.
    - Utilize um loop for para iterar de 1 a N e some todos os números pares.
    - Imprima o resultado da soma.


Exemplo de Saída:

Digite um número inteiro positivo: 10
A soma dos números pares de 1 até 10 é: 30
"""

# Solicitando ao usuário o número
N = int(input("Digite um número inteiro positivo: "))
Soma_Pares = 0
for i in range (1, N + 1):
    if i % 2 == 0:
        print(f"número: {i} + {Soma_Pares} = {i + Soma_Pares}")
        Soma_Pares += i

print(f"A soma dos números pares de 1 até {N} é: {Soma_Pares}")
