import serial
import time
import json
import csv
from datetime import datetime

#   CONFIGURATION

PORT = "COM3"
BAUD_RATE = 9600 # Must match Serial.begin(9600) in Arduino sketch
OUTPUT_FILE = "sensor_log.csv"

#   CONNECT

ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
time.sleep(2)   # Wait for Arduino to reset after connection
print(f"Connected to {PORT}")

#   CSV SETUP

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp","temp","humidity","distance","light"])

#   READ LOOP

try:
    while True:
        line = ser.readline().decode("utf-8").strip()

        if line:    # Skip empty lines
            try:
                data = json.loads(line)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                print(f"{timestamp} |)"
                      f"Temp: {data['temp']}°C |"
                      f"Humidity: {data['humidity']}% |"
                      f"Distance: {data['distance']}cm |"
                      f"Light: {data['light']}")
                
                with open(OUTPUT_FILE, "a", newline = "") as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        timestamp,
                        data["temp"],
                        data["humidity"],
                        data["distance"],
                        data["light"]
                    ])

            except json.JSONDecodeError:
                print(f"Invalid JSON: {line}")

except KeyboardInterrupt:
    ser.close()
    print("Connection closed")

