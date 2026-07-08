# ─────────────────────────────────────────────────────────────────────
#  Example 02 — Forward and Backward
#  Category  : Movement / 2WD
#  Level     : Beginner
#
#  The robot drives forward 30 cm, pauses, then returns to its
#  starting position by driving backward 30 cm.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(50)

# Drive forward
titan.moveForward(30, 'cm', True)

# Short pause so you can see the robot stop
time.sleep(0.5)

# Drive back to start
titan.moveBackward(30, 'cm', True)

titan.stopMoving()

titan.End()
