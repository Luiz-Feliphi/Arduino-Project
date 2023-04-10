#include "dht.h" //INCLUSÃO DE BIBLIOTECA
#include "Arduino.h"
 
const int pinoDHT11 = A0; //PINO ANALÓGICO UTILIZADO PELO DHT11
const int relayPin = 7;
const int relayPin2 = 4;
 dht DHT; //VARIÁVEL DO TIPO DHT
 
void setup(){ 
  pinMode(relayPin, OUTPUT);
  pinMode(relayPin2, OUTPUT);
  Serial.begin(9600); //INICIALIZA A SERIAL
  delay(2000); //INTERVALO DE 2 SEGUNDO ANTES DE INICIAR
}
 
void loop(){ 
  DHT.read11(pinoDHT11); //LÊ AS INFORMAÇÕES DO SENSOR
  Serial.print("Umidade: "); //IMPRIME O TEXTO NA SERIAL
  Serial.print(DHT.humidity); //IMPRIME NA SERIAL O VALOR DE UMIDADE MEDIDO
  Serial.print("%"); //ESCREVE O TEXTO EM SEGUIDA
  Serial.print(" / Temperatura: "); //IMPRIME O TEXTO NA SERIAL
  Serial.print(DHT.temperature, 0); //IMPRIME NA SERIAL O VALOR DE UMIDADE MEDIDO E REMOVE A PARTE DECIMAL
  Serial.println("*C"); //IMPRIME O TEXTO NA SERIAL   
  delay(2000); //INTERVALO DE 2 SEGUNDOS * NÃO DIMINUIR ESSE VALOR
  if(DHT.humidity > 70){
    digitalWrite(relayPin,HIGH);
    digitalWrite(relayPin2,LOW);    
  }else{
    digitalWrite(relayPin,LOW);  
    digitalWrite(relayPin2,HIGH);  
  }
}
