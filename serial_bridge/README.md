# Serial Bridge

Reads real-time sensor data from Arduino over Serial,
parses JSON and logs to CSV.

## Requirements
```bash
pip install pyserial

## How to Run

1. Upload sensor station sketch to Arduino
2. Close Arduino IDE Serial Monitor
3. Run: python serial_bridge.py
4. Stop with Ctrl+C — data saved to sensor_log.csv

## Output

sensor_log.csv — timestamped sensor readings
timestamp,temp,humidity,distance,light
2026-04-14 23:19:22,26.0,52.0,278.04,453

## Wiring
Component	Pin
DHT11	2
HC-SR04-TRIG	4
HC-SR04-ECHO	5
LDR	A0
LCD-RS	7
LCD-EN	8
LCD-D4_D7	9-12
