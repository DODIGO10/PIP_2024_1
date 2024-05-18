int pin_echo = 13
int ping_trig = 12

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pin_trig,OUTPUT);
  pinMode(pin_Mode,INPUT);

}

int pulso,cm;
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(pin_trig,LOW);
  delayMicroseconds(2);
  digitalWrite(pin_trig,HIGH);
  delayMicroseconds(10);
  digital(pin_trig,LOW);
  pulso =

}
