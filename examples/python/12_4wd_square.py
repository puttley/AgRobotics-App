# ─────────────────────────────────────────────────────────────────────
#  Example 12 — 4WD Square Pattern
#  Category  : Movement / 4WD
#  Level     : Beginner
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors4WD(1, 2, 3, 4)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(50)

for side in range(4):
    ag.moveForward(30, 'cm', True)
    ag.turnDegrees('right', 90, True)

ag.stopMoving()

ag.End()
