# Exercício: Palavras com Mais de 4 Letras

# Objetivo: Solicite ao usuário uma lista de palavras e, em 
# seguida, exiba apenas as palavras que têm mais de 4 letras.

# Instruções:

#     1. Peça ao usuário que insira palavras separadas 
#     por vírgula (por exemplo, ["casa","carro","sol","árvore"]).
    
#     2. Use um loop for para iterar sobre essa lista de palavras.
    
#     3. Dentro do loop, verifique o comprimento de cada palavra.
    
#     4. Se a palavra tiver mais de 4 letras, imprima-a.

# Após concluir o exercício, se o usuário inserir "casa,carro,sol,árvore", a saída deve ser:

# carro
# árvore

# palavras = input("Digite uma lista de palavras separadas por vírgula: ")
# for palavra in palavras.split(","):
#     if len(palavra) > 4:
#         print(palavra)
# print("Fim do programa")

# palavras = ["casa", "carro", "sol", "árvore"]
# for palavra in palavras:
#     if len(palavra) > 4:
#         print(palavra)