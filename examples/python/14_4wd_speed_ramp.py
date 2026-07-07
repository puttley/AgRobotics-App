# ─────────────────────────────────────────────────────────────────────
#  Example 14 — 4WD Speed Ramp
#  Category  : Movement / 4WD
#  Level     : Intermediate
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors4WD(1, 2, 3, 4)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)

ag.setMovementSpeed(20)
ag.startMoving('forward')

for speed in range(20, 81, 10):
    ag.setMovementSpeed(speed)
    print('Speed:', speed, '%')
    time.sleep(0.4)

time.sleep(1.0)

for speed in range(80, 19, -10):
    ag.setMovementSpeed(speed)
    print('Speed:', speed, '%')
    time.sleep(0.4)

ag.stopMoving()

ag.End()
