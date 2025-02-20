#Aula 127 - Abrir Navegador
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Caminho correto do ChromeDriver
caminho_driver = r"C:\Users\Joden\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Criar serviço do ChromeDriver
service = Service(caminho_driver)

# Inicializa o Chrome
abrirNavegador = webdriver.Chrome(service=service)

# Abre o Google
abrirNavegador.get("https://www.google.com/")

# Mantém aberto
input("Pressione Enter para sair...")
