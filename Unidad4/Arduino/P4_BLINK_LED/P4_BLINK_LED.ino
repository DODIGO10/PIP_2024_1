//EL ARDUINO POSEE UN LED INTERNO DE PRUEBAS EN EL PIN DIGITAL 13..
int led = 13;// 2, 3, 4, 5 ... 13

//ARDUINO TIENE 14 PINES DIGITALES ...  QUE VAN DE 0 AL 13
//SIN EMBARGO, CUANDO SE UTILIZA COMUNICACION SERIAL NO SE PUEDEN UTILIZAR
//LOS PINES 0 Y 1 COMO PINES DIGITALES

void setup() {
  // put your setup code here, to run once:
  //SE DEBE DEFINIR EL MOODO DE TRABAJO(ENTREDA O SALIDA) DE TODOS LOS PINES DIGITALES
  pinMOde(led, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led, HIGH);
  delay(1000);
  digitalWrite(led, LOW);
  delay(1000);

}
