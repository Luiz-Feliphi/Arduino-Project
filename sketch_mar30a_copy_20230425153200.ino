#include <VarSpeedServo.h>

VarSpeedServo servoMotor; // Cria um objeto para o servo motor
int pos = 0;              // Variável que armazena a posição atual do servo

void setup() {
  servoMotor.attach(11); // Define o pino do servo motor
  servoMotor.write(60); // Angulo Reto
  delay(5000);
}

void loop() {
  // Move o servo de 0 a 47 graus com velocidade crescente
  for (pos = 0; pos <= 85; pos += 1) {
    servoMotor.write(pos, 30, true);// Define a posição, a velocidade (0-255) e a direção (true para avançar) do servo
    delay(15);                      // Aguarda um curto período de tempo
    Serial.println(pos);    
  }
  // Move o servo de 97 a 0 graus com velocidade decrescente
  for (pos = 60; pos >= 0; pos -= 1) {
    servoMotor.write(pos, 30, true); // Define a posição, a velocidade (0-255) e a direção (true para avançar) do servo
    delay(15);                 // Aguarda um curto período de tempo
    Serial.println(pos); 
  }
}
