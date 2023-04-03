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

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

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

    // NOTE ON
    if (statusbyte.equals("Motor 1 on")) {
      Serial.print("Motor 1 on \n");
      digitalWrite(relay1, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (statusbyte.equals("Motor 2 on")) {
      Serial.print("Motor 2 on \n");
      digitalWrite(relay2, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 3 on")) {
      Serial.print("Motor 3 on \n");
      digitalWrite(relay3, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 4 on")) {
      Serial.print("Motor 4 on \n");
      digitalWrite(relay4, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
     else if (statusbyte.equals("Motor 5 on")) {
      Serial.print("Motor 5 on \n");
      digitalWrite(relay5, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (statusbyte.equals("Motor 6 on")) {
      Serial.print("Motor 6 on \n");
      digitalWrite(relay6, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 7 on")) {
      Serial.print("Motor 7 on \n");
      digitalWrite(relay7, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 8 on")) {
      Serial.print("Motor 8 on \n");
      digitalWrite(relay8, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }   
    else if  (statusbyte.equals("Motor 9 on")) {
      Serial.print("Motor 9 on \n");
      digitalWrite(relay9, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
     else if (statusbyte.equals("Motor 10 on")) {
      Serial.print("Motor 10 on \n");
      digitalWrite(relay10, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (statusbyte.equals("Motor 11 on")) {
      Serial.print("Motor 11 on \n");
      digitalWrite(relay11, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 12 on")) {
      Serial.print("Motor 12 on \n");
      digitalWrite(relay12, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 13 on")) {
      Serial.print("Motor 13 on \n");
      digitalWrite(relay13, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }   
    else if  (statusbyte.equals("Motor 14 on")) {
      Serial.print("Motor 14 on \n");
      digitalWrite(relay14, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
     else if (statusbyte.equals("Motor 15 on")) {
      Serial.print("Motor 15 on \n");
      digitalWrite(relay15, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (statusbyte.equals("Motor 16 on")) {
      Serial.print("Motor 16 on \n");
      digitalWrite(relay16, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 17 on")) {
      Serial.print("Motor 17 on \n");
      digitalWrite(relay17, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 18 on")) {
      Serial.print("Motor 18 on \n");
      digitalWrite(relay18, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }   
    else if  (statusbyte.equals("Motor 19 on")) {
      Serial.print("Motor 19 on \n");
      digitalWrite(relay19, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 20 on")) {
      Serial.print("Motor 20 on \n");
      digitalWrite(relay20 , LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
     else if (statusbyte.equals("Motor 21 on")) {
      Serial.print("Motor 21 on \n");
      digitalWrite(relay21, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (statusbyte.equals("Motor 22 on")) {
      Serial.print("Motor 22 on \n");
      digitalWrite(relay22, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 23 on")) {
      Serial.print("Motor 23 on \n");
      digitalWrite(relay23, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 24 on")) {
      Serial.print("Motor 24 on \n");
      digitalWrite(relay24, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (statusbyte.equals("Motor 25 on")) {
      Serial.print("Motor 25 on \n");
      digitalWrite(relay25, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }

    // NOTE OFF          
    else if (statusbyte.equals("Motor 1 off")) {
      Serial.print("Motor 1 off \n");
      digitalWrite(relay1, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (statusbyte.equals("Motor 2 off")) {
      Serial.print("Motor 2 off \n");
      digitalWrite(relay2, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 3 off")) {
      Serial.print("Motor 3 off \n");
      digitalWrite(relay3, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 4 off")) {
      Serial.print("Motor 4 off ");
      digitalWrite(relay4, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (statusbyte.equals("Motor 5 off")) {
      Serial.print("Motor 5 off \n");
      digitalWrite(relay5, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (statusbyte.equals("Motor 6 off")) {
      Serial.print("Motor 6 off \n");
      digitalWrite(relay6, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 7 off")) {
      Serial.print("Motor 7 off \n");
      digitalWrite(relay7, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 8 off")) {
      Serial.print("Motor 8 off ");
      digitalWrite(relay8, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (statusbyte.equals("Motor 9 off")) {
      Serial.print("Motor 9 off \n");
      digitalWrite(relay9, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (statusbyte.equals("Motor 10 off")) {
      Serial.print("Motor 10 off \n");
      digitalWrite(relay10, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 11 off")) {
      Serial.print("Motor 11 off \n");
      digitalWrite(relay11, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 12 off")) {
      Serial.print("Motor 12 off ");
      digitalWrite(relay12, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (statusbyte.equals("Motor 13 off")) {
      Serial.print("Motor 13 off \n");
      digitalWrite(relay13, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (statusbyte.equals("Motor 14 off")) {
      Serial.print("Motor 14 off \n");
      digitalWrite(relay14, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 15 off")) {
      Serial.print("Motor 15 off \n");
      digitalWrite(relay15, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 16 off")) {
      Serial.print("Motor 16 off ");
      digitalWrite(relay16, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (statusbyte.equals("Motor 17 off")) {
      Serial.print("Motor 17 off \n");
      digitalWrite(relay17, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (statusbyte.equals("Motor 18 off")) {
      Serial.print("Motor 18 off \n");
      digitalWrite(relay18, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 19 off")) {
      Serial.print("Motor 19 off \n");
      digitalWrite(relay19, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 20 off")) {
      Serial.print("Motor 20 off ");
      digitalWrite(relay20, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (statusbyte.equals("Motor 21 off")) {
      Serial.print("Motor 21 off \n");
      digitalWrite(relay21, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (statusbyte.equals("Motor 22 off")) {
      Serial.print("Motor 22 off \n");
      digitalWrite(relay22, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 23 off")) {
      Serial.print("Motor 23 off \n");
      digitalWrite(relay23, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 24 off")) {
      Serial.print("Motor 24 off \n");
      digitalWrite(relay24, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (statusbyte.equals("Motor 25 off")) {
      Serial.print("Motor 25 off \n");
      digitalWrite(relay25, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}
