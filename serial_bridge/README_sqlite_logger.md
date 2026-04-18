1. SQLite Sensor Logger

Reads real-time sensor data from Arduino over Serial and logs to a SQLite database.

2. Requirements
```bash
pip install pyserial

3. How to Run
Log data: python sqlite_logger.py
Query data: python query_db.py

#### Database Schema
CREATE TABLE readings (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    temp      REAL,
    humidity  REAL,
    distance  REAL,
    light     INTEGER
)

4. Wiring
DHT11 PIN2
HC-SR04_TRIG PIN4
HC-SR04_ECHO PIN5
LDR	A0
LCD_RS	PIN7
LCD_EN	PIN8
LCD_D4-D7	PIN9-12

