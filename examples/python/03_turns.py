# ─────────────────────────────────────────────────────────────────────
#  Example 03 — Turns
#  Category  : Movement / 2WD
#  Level     : Beginner
#
#  Shows how to turn left and right using encoder-based turns.
#  The robot turns right 90 degrees, drives forward, then
#  turns left 90 degrees and drives forward again.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(50)

# Move forward, turn right, move forward, turn left
ag.moveForward(20, 'cm', True)
ag.turnDegrees('right', 90, True)
ag.moveForward(20, 'cm', True)
ag.turnDegrees('left', 90, True)
ag.moveForward(20, 'cm', True)

ag.stopMoving()

ag.End()
