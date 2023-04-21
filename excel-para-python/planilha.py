import openpyxl
import gspread
from gspread_dataframe import set_with_dataframe
import time

# Defina o ID da planilha do Google que você deseja enviar os dados
id_planilha_google = "id-da-planilha-do-google"

# Defina o nome da planilha Excel que contém os dados que você deseja enviar
nome_planilha_excel = "planilha-excel.xlsx"

# Abra a planilha Excel usando o openpyxl
workbook = openpyxl.load_workbook(nome_planilha_excel)
worksheet = workbook.active

# Leia os dados da planilha Excel em uma lista de listas
dados_excel = []
for row in worksheet.iter_rows(values_only=True):
    dados_excel.append(list(row))

# Conecte-se à planilha do Google usando suas credenciais
gc = gspread.service_account(filename='conta-serviço.json')
sh = gc.open_by_key(id_planilha_google)

# Selecione a primeira planilha da planilha do Google
worksheet = sh.get_worksheet(0)

# Envie os dados da planilha Excel para a planilha do Google
for i in range(len(dados_excel)):
    try:
        values = dados_excel[i]
        worksheet.append_row(values)
        print(f"Enviando linha {i+1}")
    except gspread.exceptions.APIError as e:
        # Se não houver conexão com a Internet, pare o envio de dados e tente novamente após um intervalo de tempo
        if "Unable to fetch URL" in str(e):
            print("Sem conexão com a Internet. Aguardando...")
            while True:
                try:
                    gc = gspread.service_account(filename='conta-serviço.json')
                    sh = gc.open_by_key(id_planilha_google)
                    worksheet = sh.get_worksheet(0)
                    break
                except gspread.exceptions.APIError:
                    time.sleep(10)  # Aguarde 10 segundos antes de tentar novamente
                    continue
            # Quando a conexão com a Internet for estabelecida novamente, retome o envio de dados
            print("Conexão com a Internet estabelecida. Retomando envio de dados...")
            continue
        else:
            raise e

print("Envio de dados concluído com sucesso!")
