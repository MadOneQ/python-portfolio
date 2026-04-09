# Smart Sensor Station v1

## What it does
Reads temperature, humidity, light and distance every 2 seconds
and broadcasts structured JSON over Serial at 9600 baud.

## Output format
{"temp":25.9,"hum":49.0,"light":433,"distance":6.1,"ts":18239}

## Hardware
- Arduino Uno (Elegoo)
- DHT11 3-pin module        → Digital Pin 2
- Photoresistor + 10kΩ      → Analog Pin A0
- HC-SR04 ultrasonic sensor → Digital Pins 9 (TRIG) & 10 (ECHO)

## Wiring
| Component    | Pin        | Arduino    |
|-------------|------------|------------|
| DHT11       | VCC        | 5V         |
| DHT11       | GND        | GND        |
| DHT11       | DATA       | Digital 2  |
| LDR         | Leg 1      | 5V         |
| LDR         | Leg 2      | A0         |
| 10kΩ        | Leg 1      | A0         |
| 10kΩ        | Leg 2      | GND        |
| HC-SR04     | VCC        | 5V         |
| HC-SR04     | GND        | GND        |
| HC-SR04     | TRIG       | Digital 9  |
| HC-SR04     | ECHO       | Digital 10 |

## Concepts
- Voltage divider (LDR)
- Pulse timing (HC-SR04)
- Custom functions (getDistance())
- Multi-sensor JSON stream

## Next step
Week 3: Python pyserial bridge reads and stores this JSON stream
