
# ### **`if`**
# - **Finalidade**: Verifica uma condição única.
# - **Quando usar**: Quando precisa executar algo se uma condição for verdadeira.
# - **Exemplo**:
#   ```python
#   idade = 18
#   if idade >= 18:
#       print("Maior de idade")
#   ```
# - **Observações**:
#   - A condição no `if` deve sempre resultar em `True` ou `False`.
#   - Use operadores lógicos (`and`, `or`, `not`) para combinar condições.

# ---

# ### **`else`**
# - **Finalidade**: Executa um bloco de código caso a condição do `if` seja falsa.
# - **Quando usar**: Para definir uma alternativa ao `if`.
# - **Exemplo**:
#   ```python
#   idade = 16
#   if idade >= 18:
#       print("Maior de idade")
#   else:
#       print("Menor de idade")
#   ```
# - **Observações**:
#   - O `else` é opcional. O código funcionará sem ele, mas sem uma alternativa.
#   - Certifique-se de que o `else` esteja alinhado com o `if` correto.

# ---

# ### **`elif`**
# - **Finalidade**: Verifica múltiplas condições.
# - **Quando usar**: Quando precisa checar várias condições em sequência.
# - **Exemplo**:
#   ```python
#   nota = 6
#   if nota >= 7:
#       print("Aprovado")
#   elif nota >= 5:
#       print("Recuperação")
#   else:
#       print("Reprovado")
#   ```
# - **Observações**:
#   - Use `elif` para evitar múltiplos `if` independentes que verificam as mesmas variáveis.
#   - O `elif` só será executado se as condições anteriores forem falsas.

# ---

# ### **`while`**
# - **Finalidade**: Repetição baseada em condição.
# - **Quando usar**: Quando precisa repetir algo enquanto uma condição for verdadeira.
# - **Exemplo**:
#   ```python
#   numero = 5
#   while numero > 0:
#       print(numero)
#       numero -= 1
#   ```
# - **Observações**:
#   - Tome cuidado para evitar **loops infinitos**. Garanta que a condição eventualmente se torne falsa.
#   - Use `break` para sair do loop quando necessário.

# ---

# ### **`for`**
# - **Finalidade**: Itera sobre uma sequência ou intervalo.
# - **Quando usar**: Quando sabe quantas vezes precisa repetir ou para iterar em listas, tuplas, etc.
# - **Exemplo**:
#   ```python
#   lista = ["Ana", "João", "Maria"]
#   for nome in lista:
#       print(f"Olá, {nome}!")
#   ```
# - **Observações**:
#   - O `for` funciona bem com objetos iteráveis como listas, strings, dicionários, etc.
#   - Use `enumerate` para obter o índice junto com o elemento:
#     ```python
#     for i, nome in enumerate(lista):
#         print(f"Índice {i}: {nome}")
#     ```

# ---

# ### **`break`**
# - **Finalidade**: Interrompe o loop imediatamente.
# - **Quando usar**: Para sair de um loop antes que ele termine.
# - **Exemplo**:
#   ```python
#   for numero in range(10):
#       if numero == 5:
#           break
#       print(numero)
#   ```
# - **Observações**:
#   - O `break` funciona em ambos os loops `for` e `while`.
#   - Use com cuidado, pois pode dificultar o entendimento da lógica do loop.

# ---

# ### **`continue`**
# - **Finalidade**: Pula para a próxima iteração do loop.
# - **Quando usar**: Para ignorar o restante do código na iteração atual.
# - **Exemplo**:
#   ```python
#   for numero in range(5):
#       if numero == 2:
#           continue
#       print(numero)
#   ```
# - **Observações**:
#   - Evite usar `continue` em loops muito complexos, pois pode dificultar a leitura do código.

# ---

# ### **`pass`**
# - **Finalidade**: Placeholder vazio.
# - **Quando usar**: Quando precisa de um bloco de código vazio.
# - **Exemplo**:
#   ```python
#   if True:
#       pass
#   ```
# - **Observações**:
#   - O `pass` é útil em situações onde o código será implementado posteriormente.
#   - Não faz nada além de evitar erros de sintaxe.

# ---

# ### **`try` / `except`**
# - **Finalidade**: Captura e lida com exceções.
# - **Quando usar**: Quando espera que algo possa gerar um erro.
# - **Exemplo**:
#   ```python
#   try:
#       resultado = 10 / 0
#   except ZeroDivisionError:
#       print("Erro: divisão por zero.")
#   ```
# - **Observações**:
#   - Sempre use exceções específicas como `ZeroDivisionError` para capturar erros previsíveis.
#   - Evite capturar exceções genéricas como `except Exception`, pois pode mascarar erros inesperados.

# ---

# ### **finally**
# - **Finalidade**: Executa código independentemente de erros.
# - **Quando usar**: Para ações de limpeza, como fechar arquivos ou liberar recursos.
# - **Exemplo**:
#   ```python
#   try:
#       resultado = 10 / 0
#   except ZeroDivisionError:
#       print("Erro.")
#   finally:
#       print("Fim do programa.")
#   ```
# - **Observações**:
#   - O `finally` é sempre executado, mesmo que haja um `return` no bloco `try` ou `except`.

# ---

# ### **`lambda`**
# - **Finalidade**: Cria funções pequenas e anônimas.
# - **Quando usar**: Para operações simples, como em funções de ordem superior.
# - **Exemplo**:
#   ```python
#   dobro = lambda x: x * 2
#   print(dobro(4))
#   ```
# - **Observações**:
#   - Use lambdas apenas para lógica simples. Funções regulares são mais legíveis em casos complexos.

# ---

# ### **`with`**
# - **Finalidade**: Gerencia contextos automaticamente, como arquivos.
# - **Quando usar**: Para garantir que arquivos sejam fechados corretamente.
# - **Exemplo**:
#   ```python
#   with open("arquivo.txt", "w") as arquivo:
#       arquivo.write("Olá, Mundo!")
#   ```
# - **Observações**:
#   - O `with` evita que você esqueça de fechar arquivos, mesmo que ocorra um erro.

# ---

# ### **`yield`**
# - **Finalidade**: Pausa uma função e retorna um valor temporário.
# - **Quando usar**: Para criar geradores que produzem valores sob demanda.
# - **Exemplo**:
#   ```python
#   def contador():
#       for i in range(3):
#           yield i

#   for numero in contador():
#       print(numero)
#   ```
# - **Observações**:
#   - O `yield` permite criar funções que economizam memória ao gerar valores um por um.

# ---

# Essas observações ajudam a evitar erros e a usar cada comando de forma mais eficiente. Se quiser mais detalhes, é só avisar! 😊