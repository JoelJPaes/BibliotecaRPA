# 3. Extração de Endereços do Site dos Correios
# Descrição: Criar um script que consulta automaticamente o site dos Correios para buscar endereços com base em CEPs fornecidos em um arquivo Excel e salva os resultados em outro arquivo Excel.

# Código do Projeto:

# Este exemplo usa as bibliotecas requests, pandas e openpyxl.

import requests
from bs4 import BeautifulSoup
import pandas as pd

def buscar_endereco(cep):
    """Busca o endereço correspondente a um CEP no site dos Correios."""
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            return dados["logradouro"], dados["bairro"], dados["localidade"], dados["uf"]
    return None, None, None, None

def processar_ceps(input_excel, output_excel):
    """Processa uma lista de CEPs e salva os endereços em um arquivo Excel."""
    # Carregar os CEPs do arquivo Excel
    df = pd.read_excel(input_excel)
    df["Logradouro"] = ""
    df["Bairro"] = ""
    df["Cidade"] = ""
    df["Estado"] = ""

    # Buscar os endereços
    for i, row in df.iterrows():
        cep = str(row["CEP"]).zfill(8)  # Garante que o CEP tenha 8 dígitos
        logradouro, bairro, cidade, estado = buscar_endereco(cep)
        df.at[i, "Logradouro"] = logradouro
        df.at[i, "Bairro"] = bairro
        df.at[i, "Cidade"] = cidade
        df.at[i, "Estado"] = estado
        print(f"Processado CEP: {cep}")

    # Salvar o resultado em um novo arquivo Excel
    df.to_excel(output_excel, index=False)
    print(f"Endereços salvos em: {output_excel}")

# Automação
if __name__ == "__main__":
    input_excel = "ceps.xlsx"  # Arquivo de entrada com uma coluna "CEP"
    output_excel = "enderecos.xlsx"  # Arquivo de saída com os endereços
    processar_ceps(input_excel, output_excel)
