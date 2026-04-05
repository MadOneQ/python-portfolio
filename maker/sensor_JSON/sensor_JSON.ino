#include <DHT.h>

// Configuration
#define DHTPIN 2   // DATA wire is on digital pin 2
#define DHTTYPE DHT11   // We're using DHT 11 not DHT 22

// Create the sensor object
DHT dht(DHTPIN, DHTTYPE);

// Setup: runs once at start
void setup(){
  Serial.begin(9600);   // Open serial communication at 9600 baud
  dht.begin();    // Start the sensor
  Serial.println("DHT11 ready.");
}

// Loop: runs forever
void loop(){
  delay (2000);   // DHT 11 needs 2 seconds between readings

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();    // Celsius by default

  // Check if reading failed
  if(isnan(humidity) || isnan(temperature)) {
    Serial.println("{\"error\":\"Failed to read DHT11\"}");
    return;   // Skip the rest of this loop iteration
  }

  // Print to Serial Monitor
  Serial.print("{\"temp\":");
  Serial.print(temperature, 1);   // 1 decimal place
  Serial.print(",\"hum\":");
  Serial.print(humidity, 1);    // 1 decimal place
  Serial.print(",\"ts\":");
  Serial.print(millis());   // milliseconds since boot
  Serial.println("}");
}