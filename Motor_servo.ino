#include <Servo.h>  // Incluye la librería Servo para controlar el servo motor

Servo servoMotor;  // Crea un objeto de tipo Servo llamado servoMotor
int ang;  // Declara una variable entera para el ángulo del servo

void setup(){
  servoMotor.attach(9);  // Conecta el servo motor al pin digital 9 del Arduino
}

void loop(){
  // Mueve el servo de 0 a 180 grados
  for(ang = 0; ang < 180; ang++){
    servoMotor.write(ang);  // Establece el ángulo del servo motor
    delay(20);  // Espera 20 milisegundos para suavizar el movimiento
  }
  delay(1000);  // Espera 1 segundo al llegar a 180 grados

  // Mueve el servo de 180 a 0 grados
  for(ang = 180; ang > 0; ang--){
    servoMotor.write(ang);  // Establece el ángulo del servo motor
    delay(20);  // Espera 20 milisegundos para suavizar el movimiento
  }
  delay(1000);  // Espera 1 segundo al llegar a 0 grados
}


