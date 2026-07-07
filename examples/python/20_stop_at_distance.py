# ─────────────────────────────────────────────────────────────────────
#  Example 20 — Stop at Distance
#  Category  : Sensors + Movement
#  Level     : Intermediate
#
#  The robot drives forward until the TOF sensor detects an object
#  closer than 150mm, then stops.
#  Great introduction to sensor-triggered movement!
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(40)

STOP_DISTANCE = 150   # stop when object is closer than 150mm

print('Driving forward — will stop when object detected within', STOP_DISTANCE, 'mm')

ag.startMoving('forward')

while True:
    distance = ag.getTOFSensor(1)
    print('Distance:', distance, 'mm')
    if distance < STOP_DISTANCE:
        break
    time.sleep(0.05)

ag.stopMoving()
print('Object detected — stopped!')

ag.End()
