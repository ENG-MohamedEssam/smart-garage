#include <LiquidCrystal.h>
#include <Servo.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
Servo myservo;
int x; //byte sent from python
int servVal;
int Yindex = 0;


void setup() {
  // put your setup code here, to run once:
    myservo.attach(9);
    Serial.begin(9600);
    Serial.setTimeout(1);
    lcd.begin(16, 2);
    
  // Print a message to the LCD.
}

void loop() {
  // put your main code here, to run repeatedly:
  lcd.setCursor(0,0); 
  lcd.print("Available Spots");
  while (!Serial.available());
  x = Serial.readString().toInt();
  Serial.print(x);
  if (x == 9)
  {
     myservo.write(180);
     lcd.clear();
     lcd.setCursor(0,1);
     lcd.print("No More Places");
     delay(500);
  }
  else 
  {
    myservo.write(90);
    delay(15);
    lcd.setCursor(Yindex,1);
    lcd.print(x); 
  }
  Yindex +=2;
  if (Yindex > 11 || x == 0 || x == 8)
  {
    Yindex = 0;
    lcd.clear();
  }
}
