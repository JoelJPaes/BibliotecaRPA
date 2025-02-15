# 2. Extração de Dólar e Euro da Internet
# Descrição: Um script que extrai as cotações do dólar e do euro de um site de câmbio e salva as informações em um arquivo Excel com gráficos.

# Código do Projeto:

# Este exemplo usa a biblioteca requests para fazer a requisição ao site e openpyxl para criar o arquivo Excel.
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference

def obter_cotacao():
    """Obtém as cotações do Dólar e do Euro de um site de câmbio."""
    url = "https://www.google.com/search?q=cotação+dólar+euro"  # Site para obter os dados
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Exemplo de seleção de valores (ajustar se necessário para o site real)
    cotacao_dolar = soup.find("span", {"data-value": True}).text.strip()
    cotacao_euro = soup.find_all("span", {"data-value": True})[1].text.strip()

    return float(cotacao_dolar.replace(",", ".")), float(cotacao_euro.replace(",", "."))

def salvar_dados_excel(dados):
    """Salva as cotações em um arquivo Excel e cria um gráfico."""
    wb = Workbook()
    ws = wb.active
    ws.title = "Cotações"

    # Adiciona cabeçalhos
    ws.append(["Data", "Dólar (R$)", "Euro (R$)"])
    
    # Adiciona os dados
    for data, dolar, euro in dados:
        ws.append([data, dolar, euro])
    
    # Criar gráfico
    chart = LineChart()
    chart.title = "Cotação Dólar vs Euro"
    chart.x_axis.title = "Data"
    chart.y_axis.title = "Cotação (R$)"
    dados_grafico = Reference(ws, min_col=2, max_col=3, min_row=1, max_row=len(dados) + 1)
    chart.add_data(dados_grafico, titles_from_data=True)
    ws.add_chart(chart, "E5")

    # Salvar o arquivo
    wb.save("Cotações.xlsx")
    print("Arquivo Excel com cotações salvo como 'Cotações.xlsx'.")

# Automação
if __name__ == "__main__":
    from datetime import datetime

    # Obter cotação e salvar no Excel
    cotacoes = []
    for _ in range(3):  # Exemplo de três iterações para simular diferentes datas
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dolar, euro = obter_cotacao()
        cotacoes.append((data_atual, dolar, euro))
    
    salvar_dados_excel(cotacoes)
