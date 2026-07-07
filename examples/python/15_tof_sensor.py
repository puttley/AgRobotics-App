# ─────────────────────────────────────────────────────────────────────
#  Example 15 — TOF Distance Sensor
#  Category  : Sensors
#  Level     : Beginner
#
#  Reads the VL53L0X time-of-flight distance sensor and prints
#  the distance to the console every 200ms.
#  Plug the sensor into sensor port 1.
#  Watch the console as you move your hand closer and farther away!
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

print('TOF Sensor — move your hand in front of the sensor')
print('Distance is shown in millimeters (mm)')
print('')

while True:
    distance = ag.getTOFSensor(1)
    print('Distance:', distance, 'mm')
    time.sleep(0.2)

ag.End()
