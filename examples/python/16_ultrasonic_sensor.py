# ─────────────────────────────────────────────────────────────────────
#  Example 16 — Ultrasonic Distance Sensor
#  Category  : Sensors
#  Level     : Beginner
#
#  Reads the ultrasonic sensor and prints distance to the console.
#  Plug the sensor into sensor port 1.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

print('Ultrasonic Sensor — distance in cm')
print('')

while True:
    distance = titan.getSonicSensor(1)
    print('Distance:', distance, 'cm')
    time.sleep(0.2)

titan.End()
