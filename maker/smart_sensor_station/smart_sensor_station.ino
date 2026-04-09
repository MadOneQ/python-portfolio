#include <DHT.h>

// ── Pin definitions ────────────────────────
#define DHTPIN 2
#define DHTTYPE DHT11
#define TRIG_PIN 9
#define ECHO_PIN 10
#define LDR_PIN A0

// ── Objects ────────────────────────────────
DHT dht(DHTPIN, DHTTYPE);

// ── Setup ──────────────────────────────────
void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(TRIG_PIN, OUTPUT);  // TRIG sends signal
  pinMode(ECHO_PIN, INPUT);   // ECHO receives signal
  Serial.println("Sensor station ready.");
}

// ── Distance function ──────────────────────
float getDistance() {
  // Send 10 microsecond pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Measure echo return time
  long duration = pulseIn(ECHO_PIN, HIGH);

  // Convert to cm
  return duration * 0.034 / 2;
}

// ── Loop ───────────────────────────────────
void loop() {
  delay(2000);

  // Read all sensors
  float humidity    = dht.readHumidity();
  float temperature = dht.readTemperature();
  int   light       = analogRead(LDR_PIN);
  float distance    = getDistance();

  // Validate DHT11
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("{\"error\":\"Failed to read DHT11\"}");
    return;
  }

  // Output JSON
  Serial.print("{\"temp\":");
  Serial.print(temperature, 1);
  Serial.print(",\"hum\":");
  Serial.print(humidity, 1);
  Serial.print(",\"light\":");
  Serial.print(light);
  Serial.print(",\"distance\":");
  Serial.print(distance, 1);
  Serial.print(",\"ts\":");
  Serial.print(millis());
  Serial.println("}");
}
