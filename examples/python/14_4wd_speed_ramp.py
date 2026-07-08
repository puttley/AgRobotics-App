# ─────────────────────────────────────────────────────────────────────
#  Example 14 — 4WD Speed Ramp
#  Category  : Movement / 4WD
#  Level     : Intermediate
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors4WD(1, 2, 3, 4)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)

titan.setMovementSpeed(20)
titan.startMoving('forward')

for speed in range(20, 81, 10):
    titan.setMovementSpeed(speed)
    print('Speed:', speed, '%')
    time.sleep(0.4)

time.sleep(1.0)

for speed in range(80, 19, -10):
    titan.setMovementSpeed(speed)
    print('Speed:', speed, '%')
    time.sleep(0.4)

titan.stopMoving()

titan.End()
