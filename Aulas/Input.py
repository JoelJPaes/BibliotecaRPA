"""
nome = input("Digite seu nome: \n")
print("\nO seu nome é:" + nome)
"""
"""
nome = input("Digite seu nome:")
nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
media = float(nota1 + nota2) / 2

print("Aluno:",nome, "Média:", media)
"""

#exercicio
"""
nDigitado = int(input("A tabuada de qual numero deseja ver?"))
print(nDigitado, "* 1 =", nDigitado * 1)
print(nDigitado, "* 2 =", nDigitado * 2)
print(nDigitado, "* 3 =", nDigitado * 3)
print(nDigitado, "* 4 =", nDigitado * 4)
print(nDigitado, "* 5 =", nDigitado * 5)
print(nDigitado, "* 6 =", nDigitado * 6)
print(nDigitado, "* 7 =", nDigitado * 7)
print(nDigitado, "* 8 =", nDigitado * 8)
print(nDigitado, "* 9 =", nDigitado * 9)
print(nDigitado, "* 10 =", nDigitado *10)

"""
"""
anoqnasceu = int(input("ano de nascimento:"))
anocorrente = 2025
print int(input("Que ano você nasceu?", anoqnasceu))
print int("Então você tem:", anocorrente -anoqnasceu, "de idade.")
"""
"""
anoqnasceu = int(input("Ano de nascimento: "))  # Corrigido para receber corretamente o ano de nascimento
anocorrente = 2025  # Não precisa converter para int, já é um número

print("Que ano você nasceu?", anoqnasceu)  # Apenas exibindo o ano de nascimento
print("Então você tem:", anocorrente - anoqnasceu, "anos de idade.")  # Calcula e exibe a idade corretamente
"""
#correção
ano_atual = 2025
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

print("Sua idade é:", idade)

