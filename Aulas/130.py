import xlsxwriter  # Importamos o "mestre das tabelas", que nos ajudará a criar uma planilha
import os  # Chamamos o "porteiro do sistema", que nos permitirá abrir arquivos depois

# Escolhemos um endereço onde nossa planilha vai morar (caminho do arquivo)
nomeCaminhoArquivo = r"C:\Users\Joden\OneDrive\Área de Trabalho\CARREIRA PROGRAMAÇÃO\CursoPythonRPA\ExtraindoValorDolarEuroExcel\Dolar e Euro Wise.xlsx"

# Criamos um novo "livro de anotações" chamado planilhaCriada (nosso arquivo Excel)
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)

# Pegamos uma folha novinha e colocamos dentro do nosso livro
sheet1 = planilhaCriada.add_worksheet()  # Agora temos um espaço para escrever nossos dados!

# Começamos a escrever no topo da planilha, como se fosse o cabeçalho de uma tabela
sheet1.write("A1", "Nome")  # Criamos a coluna de "Nome"
sheet1.write("B1", "Idade")  # Criamos a coluna de "Idade"

# Agora começamos a preencher nossa lista com alguns dados
sheet1.write("A2", "Amanda")  # Escrevemos "Amanda" na coluna de nomes, linha 2
sheet1.write("B2", 28)  # Colocamos a idade da Amanda ao lado dela

sheet1.write("A3", "Roberto")  # Escrevemos "Roberto" na coluna de nomes, linha 3
sheet1.write("B3", 25)  # Colocamos a idade do Roberto ao lado dele

# Fechamos o livro de anotações para que todas as informações fiquem guardadas com segurança
planilhaCriada.close()  # Se não fecharmos, corremos o risco de perder os dados como num truque de mágica ruim 🎩✨

# Chamamos o "porteiro do sistema" para abrir nossa planilha e conferir se tudo ficou certinho
os.startfile(nomeCaminhoArquivo)  # Agora podemos ver nossa tabela ganhando vida!
