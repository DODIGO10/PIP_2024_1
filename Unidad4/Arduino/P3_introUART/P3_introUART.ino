
void setup() {
  // put your setup code here, to run once:
  //MODLO UART ... MODULO ASCRONO UNIVERSAL DE TRANSMISION Y RECEPCION DE DATOS
  Serial.begin(9600);//INICIALIZA LA COMUNICACION DE TRANSMISION Y RECEPCION DE DATOS
  //9600 BAUDIOS A LOS QUE SE COMUNICA ARDUINO CON OTROS DISPOSITIVOS

  //ARDUINO TRABAJA A 16MHZ ....
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hola! :D! :3");
  delay(500);//milisecs

}
