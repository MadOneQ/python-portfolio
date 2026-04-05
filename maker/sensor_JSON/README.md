# DHT11 Sensor — JSON Serial Output

## What it does
Reads temperature and humidity from a DHT11 sensor every 2 seconds
and broadcasts structured JSON over Serial at 9600 baud.

## Output format
{"temp":25.5,"hum":55.0,"ts":6069}

## Hardware
- Arduino Uno (Elegoo)
- DHT11 3-pin module
- 3x jumper wires

## Wiring
| DHT11 Pin | Arduino Pin |
|-----------|-------------|
| VCC       | 5V          |
| GND       | GND         |
| DATA      | Digital 2   |

## Libraries
- DHT sensor library by Adafruit
- Adafruit Unified Sensor

## Next step
Week 3: Python pyserial bridge will read and parse this JSON stream
