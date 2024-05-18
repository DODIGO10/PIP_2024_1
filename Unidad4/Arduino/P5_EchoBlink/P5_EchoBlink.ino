//EL ARDUINO POSEE UN LED INTERNO DE PRUEBAS EN EL PIN DIGITAL 13..
int led = 13;// 2, 3, 4, 5 ... 13
int v;

//ARDUINO TIENE 14 PINES DIGITALES ...  QUE VAN DE 0 AL 13
//SIN EMBARGO, CUANDO SE UTILIZA COMUNICACION SERIAL NO SE PUEDEN UTILIZAR
//LOS PINES 0 Y 1 COMO PINES DIGITALES

void setup() {
  Serial.begin(9600)
  pinMOde(led, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(led, HIGH);
  Serial.println("led prendido");
  delay(1000);
  digitalWrite(led, LOW);
  Serial.println("led apagado");
  delay(1000);

}
