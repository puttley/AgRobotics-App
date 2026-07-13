# ─────────────────────────────────────────────────────────────────────
#  Example 03 — Turns
#  Category  : Movement / 2WD
#  Level     : Beginner
#
#  Shows how to turn left and right using encoder-based turns.
#  The robot turns right 90 degrees, drives forward, then
#  turns left 90 degrees and drives forward again.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors2WD(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(50)

# Move forward, turn right, move forward, turn left
titan.moveForDistance(20, 'cm', True)
titan.turnDegrees('right', 90, True)
titan.moveForDistance(20, 'cm', True)
titan.turnDegrees('left', 90, True)
titan.moveForDistance(20, 'cm', True)

titan.stopMoving()

titan.End()
