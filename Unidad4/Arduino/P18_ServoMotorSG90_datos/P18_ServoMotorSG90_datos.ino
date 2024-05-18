#include <Servo.h>

int pinServo = 9;
Servo servo;

void setup() {
  Serial.begin(9600);
  servo.attach(pinServo);
}

void loop() {
  servo.write(0); 

  if (Serial.available() > 0) { 
    int valor = Serial.readString().toInt(); 

    servo.write(valor); 
    Serial.println(valor);
    delay(5000); 
  }
}
