String statusbyte;
int dt;
int relay1 = 2; // C3
int relay2 = 10;
int relay3 = 9;
int relay4 = 8;
int relay5 = 7;
int relay6 = 6;
int relay7 = 5;
int relay8 = 4;
int relay9 = 3;
int relay10 = 30;
int relay11 = 44;
int relay12 = 32;
int relay13 = 42;
int relay14 = 34;
int relay15 = 40;
int relay16 = 36;
int relay17 = 38;
int relay18 = 22;
int relay19 = 52;
int relay20 = 24;
int relay21 = 50;
int relay22 = 26;
int relay23 = 48;
int relay24 = 28;
int relay25 = 46; // c5


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
    String noteNum = parseString(statusbyte, ',', 0);
    String status = parseString(statusbyte, ',',1);


    if (status == "on") {
      runMotor(noteNum);
    }
    else if (status == "off") {
      stopMotor(noteNum);
    }
    
  }

}

String parseString(String data, char separator, int index) {
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;
 
  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  } 
 
  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void runMotor(String motorNo) {
   if (motorNo == "1") {
      //Serial.print("Motor 1 on \n");
      digitalWrite(relay1, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (motorNo == "2") {
      //Serial.print("Motor 2 on \n");
      digitalWrite(relay2, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "3") {
      //Serial.print("Motor 3 on \n");
      digitalWrite(relay3, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "4") {
      //Serial.print("Motor 4 on \n");
      digitalWrite(relay4, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
     else if (motorNo == "5") {
      //Serial.print("Motor 5 on \n");
      digitalWrite(relay5, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (motorNo == "6") {
      //Serial.print("Motor 6 on \n");
      digitalWrite(relay6, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "7") {
      //Serial.print("Motor 7 on \n");
      digitalWrite(relay7, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "8") {
      //Serial.print("Motor 8 on \n");
      digitalWrite(relay8, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }   
    else if  (motorNo == "9") {
      //Serial.print("Motor 9 on \n");
      digitalWrite(relay9, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
     else if (motorNo == "10") {
      //Serial.print("Motor 10 on \n");
      digitalWrite(relay10, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (motorNo == "11") {
      //Serial.print("Motor 11 on \n");
      digitalWrite(relay11, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "12") {
      //Serial.print("Motor 12 on \n");
      digitalWrite(relay12, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "13") {
      //Serial.print("Motor 13 on \n");
      digitalWrite(relay13, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }   
    else if  (motorNo == "14") {
      //Serial.print("Motor 14 on \n");
      digitalWrite(relay14, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
     else if (motorNo == "15") {
      //Serial.print("Motor 15 on \n");
      digitalWrite(relay15, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (motorNo == "16") {
      //Serial.print("Motor 16 on \n");
      digitalWrite(relay16, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "17") {
      //Serial.print("Motor 17 on \n");
      digitalWrite(relay17, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "18") {
      //Serial.print("Motor 18 on \n");
      digitalWrite(relay18, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }   
    else if  (motorNo == "19") {
      //Serial.print("Motor 19 on \n");
      digitalWrite(relay19, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "20") {
      //Serial.print("Motor 20 on \n");
      digitalWrite(relay20 , LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
     else if (motorNo == "21") {
      //Serial.print("Motor 21 on \n");
      digitalWrite(relay21, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (motorNo == "22") {
      //Serial.print("Motor 22 on \n");
      digitalWrite(relay22, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "23") {
      //Serial.print("Motor 23 on \n");
      digitalWrite(relay23, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "24") {
      //Serial.print("Motor 24 on \n");
      digitalWrite(relay24, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if  (motorNo == "25") {
      //Serial.print("Motor 25 on \n");
      digitalWrite(relay25, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
    }  
}

void stopMotor(String motorNo) {
   if (motorNo == "1") {
      //Serial.print("Motor 1 off \n");
      digitalWrite(relay1, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (motorNo == "2") {
      //Serial.print("Motor 2 off \n");
      digitalWrite(relay2, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "3") {
      //Serial.print("Motor 3 off \n");
      digitalWrite(relay3, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "4") {
      //Serial.print("Motor 4 off ");
      digitalWrite(relay4, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (motorNo == "5") {
      //Serial.print("Motor 5 off \n");
      digitalWrite(relay5, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (motorNo == "6") {
      //Serial.print("Motor 6 off \n");
      digitalWrite(relay6, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "7") {
      //Serial.print("Motor 7 off \n");
      digitalWrite(relay7, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "8") {
      //Serial.print("Motor 8 off ");
      digitalWrite(relay8, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (motorNo == "9") {
      //Serial.print("Motor 9 off \n");
      digitalWrite(relay9, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (motorNo == "10") {
      //Serial.print("Motor 10 off \n");
      digitalWrite(relay10, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "11") {
      //Serial.print("Motor 11 off \n");
      digitalWrite(relay11, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "12") {
      //Serial.print("Motor 12 off ");
      digitalWrite(relay12, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (motorNo == "13") {
      //Serial.print("Motor 13 off \n");
      digitalWrite(relay13, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (motorNo == "14") {
      //Serial.print("Motor 14 off \n");
      digitalWrite(relay14, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "15") {
      //Serial.print("Motor 15 off \n");
      digitalWrite(relay15, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "16") {
      //Serial.print("Motor 16 off ");
      digitalWrite(relay16, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (motorNo == "17") {
      //Serial.print("Motor 17 off \n");
      digitalWrite(relay17, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (motorNo == "18") {
      //Serial.print("Motor 18 off \n");
      digitalWrite(relay18, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "19") {
      //Serial.print("Motor 19 off \n");
      digitalWrite(relay19, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "20") {
      //Serial.print("Motor 20 off ");
      digitalWrite(relay20, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (motorNo == "21") {
      //Serial.print("Motor 21 off \n");
      digitalWrite(relay21, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if (motorNo == "22") {
      //Serial.print("Motor 22 off \n");
      digitalWrite(relay22, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "23") {
      //Serial.print("Motor 23 off \n");
      digitalWrite(relay23, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "24") {
      //Serial.print("Motor 24 off \n");
      digitalWrite(relay24, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
    else if  (motorNo == "25") {
      //Serial.print("Motor 25 off \n");
      digitalWrite(relay25, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
    }
  } 
