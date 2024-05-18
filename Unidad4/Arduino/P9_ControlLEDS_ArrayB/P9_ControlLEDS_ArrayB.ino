int led[] = {2,3,4,5,6,7,8,9};
bool estados[] ={false,false,false,false,false,false,false,false}

void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i<8; i++){
    pinMOde(leds[i],OUTPUT)
  }

  Serial.begin(9600);
  Serial.setTimeout(10);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    //CONSIDERANDO USUARIOS SEMI PERFECTOS...
    //CUALQUIER VALOR NUMERICOS >0 OR <0 --> PRENDE EL LED
    //CUALQUIER VALOR QUE NO SEA NUMERO APAGA EL LED
    int idx_led = Serial.readString().toInt() -1;
    estados[idx_led] = !estados[idx_led];
    digitalWrite(led[idx_led],estados[idx_led]);
  }

}
