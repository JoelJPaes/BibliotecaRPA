# 4. Preenchimento de Formulários Web
# Descrição: Este script automatiza o preenchimento 
# de um formulário web fictício ou real, 
# simulando o cadastro de usuários. 
# Para isso, utilizaremos a biblioteca selenium.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def preencher_formulario():
    """Preenche um formulário web automaticamente usando Selenium."""
    # Configurar o driver do navegador (Chrome neste exemplo)
    driver = webdriver.Chrome()  # Certifique-se de ter o chromedriver instalado
    url = "https://www.example.com/formulario"  # Substitua pelo URL do formulário
    driver.get(url)

    # Preencher os campos do formulário (exemplo)
    try:
        nome = driver.find_element(By.NAME, "nome")  # Substitua 'nome' pelo atributo name do campo
        email = driver.find_element(By.NAME, "email")  # Substitua 'email' pelo atributo name do campo
        mensagem = driver.find_element(By.NAME, "mensagem")  # Substitua 'mensagem' pelo atributo name do campo

        nome.send_keys("João Silva")
        email.send_keys("joao.silva@example.com")
        mensagem.send_keys("Esta é uma mensagem automatizada!")

        # Enviar o formulário
        botao_enviar = driver.find_element(By.NAME, "enviar")  # Substitua 'enviar' pelo name do botão
        botao_enviar.click()

        print("Formulário enviado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        time.sleep(5)  # Aguarda alguns segundos para visualizar o resultado
        driver.quit()

# Automação
if __name__ == "__main__":
    preencher_formulario()
