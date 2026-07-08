# ─────────────────────────────────────────────────────────────────────
#  Example 20 — Stop at Distance
#  Category  : Sensors + Movement
#  Level     : Intermediate
#
#  The robot drives forward until the TOF sensor detects an object
#  closer than 150mm, then stops.
#  Great introduction to sensor-triggered movement!
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(40)

STOP_DISTANCE = 150   # stop when object is closer than 150mm

print('Driving forward — will stop when object detected within', STOP_DISTANCE, 'mm')

titan.startMoving('forward')

while True:
    distance = titan.getTOFSensor(1)
    print('Distance:', distance, 'mm')
    if distance < STOP_DISTANCE:
        break
    time.sleep(0.05)

titan.stopMoving()
print('Object detected — stopped!')

titan.End()
