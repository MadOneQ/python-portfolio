#include <LiquidCrystal.h>
#include <DHT.h>

// PINS
#define DHTPIN 2
#define DHTTYPE DHT11
#define TRIG_PIN 4
#define ECHO_PIN 5
#define LDR_PIN A0

// OBJECTS
LiquidCrystal lcd(7,8,9,10,11,12);
DHT dht(DHTPIN, DHTTYPE);

// FUNCTIONS
float getDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH);
  return duration * 0.034 / 2;
}

int getLight() {
  return analogRead(LDR_PIN);
}

int screenMode = 0;

//  SETUP
void setup() {
  Serial.begin(9600);
  dht.begin();
  lcd.begin(16,2);  // 16 columns, 2 rows
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

// LOOP
void loop() {
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  float dist = getDistance();
  int light = getLight();

  //LCD DISPLAY
  if(screenMode == 0) {
    lcd.setCursor(0, 0);  // column 0, row 0
    lcd.print("Temp: " + String(temp, 1) + "C ");
    lcd.setCursor(0, 1);  // column 0, row 1
    lcd.print("Humid: " + String(hum, 0) + "% ");
  } else {
    lcd.setCursor(0, 0);
    lcd.print("Dist: " + String(dist, 1) + "cm ");
    lcd.setCursor(0, 1);
    lcd.print("Light: " + String(light) + " ");
  }

screenMode = (screenMode + 1) % 2;  // Toggle between 0 and 1

  // SERIAL JSON
  
  Serial.print("{\"temp\":");
    Serial.print(temp);
    Serial.print(",\"humidity\":");
    Serial.print(hum);
    Serial.print(",\"distance\":");
    Serial.print(dist);
    Serial.print(",\"light\":");
    Serial.print(light);
    Serial.println("}");

    delay(2000);
}
