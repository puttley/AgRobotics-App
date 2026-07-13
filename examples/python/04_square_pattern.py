# ─────────────────────────────────────────────────────────────────────
#  Example 04 — Square Pattern
#  Category  : Movement / 2WD
#  Level     : Beginner
#
#  The robot drives in a square — forward, turn right 90°,
#  repeated 4 times. A classic first navigation challenge!
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors2WD(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(50)

# Repeat 4 times to complete the square
for side in range(4):
    titan.moveForDistance(30, 'cm', True)
    titan.turnDegrees('right', 90, True)

titan.stopMoving()

titan.End()
