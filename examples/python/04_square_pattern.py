# ─────────────────────────────────────────────────────────────────────
#  Example 04 — Square Pattern
#  Category  : Movement / 2WD
#  Level     : Beginner
#
#  The robot drives in a square — forward, turn right 90°,
#  repeated 4 times. A classic first navigation challenge!
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(50)

# Repeat 4 times to complete the square
for side in range(4):
    ag.moveForward(30, 'cm', True)
    ag.turnDegrees('right', 90, True)

ag.stopMoving()

ag.End()
