def exibir_informações(**kwargs):

    #função que exibe informações pessoais
    for chave, valor in kwargs.items():
        print(chave + ": " + str(valor))
exibir_informações(nome="João", idade=30, cidade="São Paulo")