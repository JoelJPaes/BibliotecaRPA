"""
Exercício: Função para Calcular Estatísticas de Números

Objetivo: Familiarizar com a definição de funções que 
aceitem um número variável de argumentos usando *args, bem como calcular 
algumas estatísticas básicas de um conjunto de números.

Instruções:

    1. Defina uma função chamada estatisticas que aceite 
    um número variável de argumentos numéricos.
    
    2. A função deve retornar a média, o maior e o menor número do conjunto.
    3. Peça ao usuário para inserir uma sequência de números, separados por espaços.
    4. Converta essa entrada do usuário em uma lista de números.
    5. Use a função estatisticas para calcular a média, o maior e o menor número da lista.
    6. Mostre ao usuário a média, o maior e o menor número.
"""

def estatisticas(*args):
    
    return sum(args) / len(args), max(args), min(args)

numeros = list(map(float, input("Digite uma sequência de números separados por espaços: ").split()))

media, maior, menor = estatisticas(*numeros)

print(f"Média: {media}")
print(f"Maior Número: {maior}")
print(f"Menor Número: {menor}")
