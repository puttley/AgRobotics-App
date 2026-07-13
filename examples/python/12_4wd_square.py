# ─────────────────────────────────────────────────────────────────────
#  Example 12 — 4WD Square Pattern
#  Category  : Movement / 4WD
#  Level     : Beginner
#  4WD configurations do not turn as accurate as 2WD - turning parameters may need adjustment
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors4WD(1, 2, 3, 4)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(50)

for side in range(4):
    titan.moveForDistance(30, 'cm', True)
    titan.turnDegrees('right', 90, True)

titan.stopMoving()

titan.End()
