//Voltaje de referencia:
//Bits de resolucion: 10bits de resolucion...1024 valores posibles...

//cade valor que le da el arduino se distancia uno del otro en 4.8mV

// la señala analogica deñ arduino funciona con los pines analogicos { A#....}

int potenciometro = AB; // pin analogico A0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  //pinMode no se utiliza para pines analogicos...

  //NOTA: un pin analogico solo es entrada....
}  
//P1  P2  P3
//GND A#  5V
//    A0  

int valor;
void loop() {
  // put your main code here, to run repeatedly:
  valor = analoRead(potenciometro);
  Serial.println(valor);
  delay(100);

}
