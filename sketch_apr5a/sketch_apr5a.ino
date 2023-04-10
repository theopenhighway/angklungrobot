String statusbyte;
int relay1 = 2;
int relay2 = 3;
int relay3 = 4;
int relay4 = 5;
int relay5 = 6;
int relay6 = 7;
int relay7 = 8;
int relay8 = 9;
int relay9 = 10;
int relay10 = 11;
int relay11 = 12;
int relay12 = 13;
int relay13 = 22;
int relay14 = 24;
int relay15 = 26;
int relay16 = 28;
int relay17 = 30;
int relay18 = 32;
int relay19 = 34;
int relay20 = 36;
int relay21 = 38;
int relay22 = 40;
int relay23 = 42;
int relay24 = 44;
int relay25 = 46;
String arr[3];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(31250);

  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);
  pinMode(relay5, OUTPUT);
  pinMode(relay6, OUTPUT);
  pinMode(relay7, OUTPUT);
  pinMode(relay8, OUTPUT);
  pinMode(relay9, OUTPUT);
  pinMode(relay10, OUTPUT);
  pinMode(relay11, OUTPUT);
  pinMode(relay12, OUTPUT);
  pinMode(relay13, OUTPUT);
  pinMode(relay14, OUTPUT);
  pinMode(relay15, OUTPUT);
  pinMode(relay16, OUTPUT);
  pinMode(relay17, OUTPUT);
  pinMode(relay18, OUTPUT);
  pinMode(relay19, OUTPUT);
  pinMode(relay20, OUTPUT);
  pinMode(relay21, OUTPUT);
  pinMode(relay22, OUTPUT);
  pinMode(relay23, OUTPUT);
  pinMode(relay24, OUTPUT);
  pinMode(relay25, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

   
  digitalWrite(relay1, HIGH);
  digitalWrite(relay2, HIGH);
  digitalWrite(relay3, HIGH);
  digitalWrite(relay4, HIGH);
  digitalWrite(relay5, HIGH);
  digitalWrite(relay6, HIGH);
  digitalWrite(relay7, HIGH);
  digitalWrite(relay8, HIGH);
  digitalWrite(relay9, HIGH);
  digitalWrite(relay10, HIGH);
  digitalWrite(relay11, HIGH);
  digitalWrite(relay12, HIGH);
  digitalWrite(relay13, HIGH);
  digitalWrite(relay14, HIGH);
  digitalWrite(relay15, HIGH);
  digitalWrite(relay16, HIGH);
  digitalWrite(relay17, HIGH);
  digitalWrite(relay18, HIGH);
  digitalWrite(relay19, HIGH);
  digitalWrite(relay20, HIGH);
  digitalWrite(relay21, HIGH);
  digitalWrite(relay22, HIGH);
  digitalWrite(relay23, HIGH);
  digitalWrite(relay24, HIGH);
  digitalWrite(relay25, HIGH);   
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    statusbyte = Serial.readStringUntil('\n');
    statusbyte.trim(); 


  }

}

void parseString(String statusbyte) {
  String arr = strtok(statusbyte,",");
}

void runMotor(String motorNo, String statusbyte, String dt) {
  
}

void stopMotor(String motorNo, String statusbyte, String dt) {
  
}