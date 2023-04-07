import serial
import pandas as pd

port = "COM3"  # altere para o número da porta correspondente ao seu Arduino
baudrate = 9600  # velocidade de comunicação

# criar DataFrame do pandas com as colunas que deseja salvar os dados
data = pd.DataFrame(columns=["Timestamp", "Dados"])

try:
    arduino = serial.Serial(port, baudrate)
except serial.SerialException:
    print("Erro ao abrir a porta " + port)
else:
    print("Porta " + port + " aberta com sucesso!")

while True:
    try:
        # ler dados da porta serial
        dados = arduino.readline().decode().strip()
        print("Dados lidos: " + dados)
        
        # adicionar os dados lidos ao DataFrame
        data = data.append({"Timestamp": pd.Timestamp.now(), "Dados": dados}, ignore_index=True)
    except serial.SerialException:
        print("Erro ao ler dados da porta " + port)
        break

arduino.close()  # fechar a porta serial ao final da comunicação

# salvar o DataFrame em uma planilha Excel
data.to_excel("dados_arduino.xlsx", index=False)

#Codigo Feito na IA ChatGPT
