import sqlite3
import serial
import time
import json
from datetime import datetime

#   CONFIGURATION

PORT = "COM3"
BAUD_RATE = 9600 # Must match Serial.begin(9600) in Arduino sketch
DB_FILE = "sensor_data.db"

#   DATABASE SETUP
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            temp      REAL,
            humidity  REAL,
            distance  REAL,
            light     INTEGER,
            motion    INTEGER
        )
    """)
    conn.commit()
    return conn

#   INSERT READING
def insert_reading(conn, timestamp, temp, humidity, distance, light, motion):
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO readings (timestamp, temp, humidity, distance, light, motion)
                   VALUES (?, ?, ?, ?, ?, ?)
                   """, (timestamp, temp, humidity, distance, light, motion))
    conn.commit()

#   MAIN

def main():
    conn = init_db()
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    print(f"Connected to {PORT}.")
    print("Logging to SQLite - press Ctrl+C to stop\n")

    prev_motion = 0

    try:
        while True:
            line = ser.readline().decode("utf-8").strip()
            if line:
                try:
                    data = json.loads(line)
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    insert_reading(
                        conn,
                        timestamp,
                        data["temp"],
                        data["humidity"],
                        data["distance"],
                        data["light"],
                        data["motion"]
                    )
                    print(f"{timestamp} |"
                          f"Temp: {data['temp']}°C |"
                          f"Humidity: {data['humidity']}% |"
                          f"Distance: {data['distance']}cm |"
                          f"Light: {data['light']} |"
                          f"Motion: {data['motion']}")
                    
                    if data['motion'] == 1 and prev_motion == 0:
                        print("MOTION DETECTED")
                    if data['motion'] == 0 and prev_motion == 1:
                        print("MOTION STOPPED")
                        
                    prev_motion = data['motion']

                except json.JSONDecodeError:
                    print(f"Invalid JSON: {line}")

    except KeyboardInterrupt:
        ser.close()
        conn.close()
        print("\nConnection closed. Data saved to sensor_data.db)")

if __name__ == "__main__":
    main()