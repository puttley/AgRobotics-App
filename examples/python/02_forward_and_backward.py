# ─────────────────────────────────────────────────────────────────────
#  Example 02 — Forward and Backward
#  Category  : Movement / 2WD
#  Level     : Beginner
#
#  The robot drives forward 30 cm, pauses, then returns to its
#  starting position by driving backward 30 cm.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(50)

# Drive forward
ag.moveForward(30, 'cm', True)

# Short pause so you can see the robot stop
time.sleep(0.5)

# Drive back to start
ag.moveBackward(30, 'cm', True)

ag.stopMoving()

ag.End()
