#include <LiquidCrystal.h>
String prev = "";
const int button = 2;
int buttonState = 0;
const int led = 3;

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup()
{
    Serial.begin(9600);
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
    lcd.setCursor(0,0);
}

void loop(){
    printLCD(prev);
    String cur = Serial.readString();
    if (cur != prev) {
        prev = cur;
        lcd.clear();
    }
}

void printLCD(String cur) {
    char chars[sizeof(cur)];
    cur.toCharArray(chars, sizeof(cur));
    String l1 = cur.substring(0, cur.indexOf("    "));
    String l2 = cur.substring(cur.indexOf("    ") + 4);
    lcd.setCursor(0, 0);
    lcd.print(l1);
    lcd.setCursor(0, 1);
    lcd.print(l2);
}
