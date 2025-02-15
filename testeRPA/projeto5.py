# 5. Manipulação de Excel com XlsxWriter
# Descrição: Este script cria uma planilha Excel 
# com múltiplas abas, gráficos dinâmicos e relatórios 
# formatados, simulando, por exemplo, o controle de 
# vendas.

import xlsxwriter

def criar_planilha_excel():
    """Cria uma planilha Excel com dados simulados e gráficos usando XlsxWriter."""
    # Nome do arquivo Excel
    arquivo_excel = "Relatorio_Vendas.xlsx"

    # Criar uma pasta de trabalho e adicionar uma planilha
    workbook = xlsxwriter.Workbook(arquivo_excel)
    worksheet = workbook.add_worksheet("Vendas")

    # Dados simulados
    cabecalho = ["Produto", "Quantidade", "Preço Unitário", "Receita"]
    dados = [
        ["Produto A", 100, 20, 100 * 20],
        ["Produto B", 50, 35, 50 * 35],
        ["Produto C", 200, 15, 200 * 15],
        ["Produto D", 80, 40, 80 * 40],
    ]

    # Adicionar cabeçalho
    for col, titulo in enumerate(cabecalho):
        worksheet.write(0, col, titulo)

    # Adicionar os dados
    for row, linha in enumerate(dados, start=1):
        for col, valor in enumerate(linha):
            worksheet.write(row, col, valor)

    # Adicionar fórmula para calcular o total de receitas
    worksheet.write(len(dados) + 1, 3, "=SUM(D2:D5)")  # Fórmula Excel

    # Criar um gráfico de colunas
    chart = workbook.add_chart({"type": "column"})

    # Configurar o gráfico com os dados de receita
    chart.add_series({
        "name": "Receita por Produto",
        "categories": ["Vendas", 1, 0, len(dados), 0],  # Nome dos produtos
        "values": ["Vendas", 1, 3, len(dados), 3],  # Valores da receita
    })

    # Configurar o título e os eixos do gráfico
    chart.set_title({"name": "Receita por Produto"})
    chart.set_x_axis({"name": "Produtos"})
    chart.set_y_axis({"name": "Receita (R$)"})

    # Adicionar o gráfico à planilha
    worksheet.insert_chart("F2", chart)

    # Salvar o arquivo Excel
    workbook.close()
    print(f"Planilha '{arquivo_excel}' criada com sucesso!")

# Automação
if __name__ == "__main__":
    criar_planilha_excel()
