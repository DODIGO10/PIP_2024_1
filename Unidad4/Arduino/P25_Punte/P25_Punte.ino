//129d --- módulo
//--- 2 puentes h

//ENA --- VELOCIDAD DE GIRO
//IN1   .....SENTIDO DE GIRO
//IN2   .....
//OUT1
//OUT2

//ENB
//IN3
//IN4
//OUT3
//OUT4
int ENA = 3; //pin PWM
int in1 = 5;
int in2 = 6;

//Conectados al motor
//out 1 y out 2 se conecta directamente del puente h al motor

void setup() {
  // put your setup code here, to run once:
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  //ENA ... no lleva pinmode porque es de PWM

  Serial.begin(9600);
  Serial.setTimeout(100);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int v = Serial.readString().toInt();
    if(v == 0){
      Serial.println("Detenerse");
      digitalWrite(in1,0);
      digitalWrite(in2,0);
      analogWrite(ENA,0);
    }
    else if(v == 1){
      Serial.println("Gira izquierda");
      digitalWrite(in1,0);
      digitalWrite(in2,1);
      analogWrite(ENA,255);
    }
    else if(v == 2){
      Serial.println("gira derecha");
      Serial.println("Gira izquierda");
      digitalWrite(in1,1);
      digitalWrite(in2,0);
      analogWrite(ENA,255);
    }
    else{
      Serial.println("movimiento no valido");
    }
  }

}
