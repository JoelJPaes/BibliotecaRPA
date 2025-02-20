# Importa a biblioteca Selenium e o módulo webdriver para controlar o navegador
from selenium import webdriver

# Importa o módulo Service, que é necessário para configurar o caminho do driver do Chrome
from selenium.webdriver.chrome.service import Service

# Importa o módulo 'keys' do Selenium, que permite simular teclas do teclado
from selenium.webdriver.common.keys import Keys  

# Importa a biblioteca PyAutoGUI para pausas e interações
import pyautogui as tempoPausaComputador  

# Importa o módulo 'By', que permite localizar elementos HTML pelo Selenium
from selenium.webdriver.common.by import By  

# Define o caminho para o arquivo do driver do Chrome
caminho_driver = r"C:\Users\Joden\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Cria um serviço do ChromeDriver com o caminho especificado
service = Service(caminho_driver)

# Inicializa o navegador Chrome, passando o serviço corretamente
meuNavegador = webdriver.Chrome(service=service)

# Acessa a página de conversão de moedas do Wise
meuNavegador.get("https://wise.com/br/currency-converter/dolar-hoje")

# Aguarda 5 segundos para garantir que a página carregue completamente
tempoPausaComputador.sleep(5)

# Localiza o campo que contém o valor do dólar e extrai o valor correto
valorDolar = meuNavegador.find_element(By.XPATH, '//*[@id="target-input"]').get_attribute("value")

# Exibe o valor do dólar capturado
print(f"Valor do dólar hoje pelo wise: {valorDolar}")

# Aguarda o usuário pressionar Enter antes de fechar o navegador
input("Pressione Enter para sair...")

# Fecha o navegador
meuNavegador.quit()
