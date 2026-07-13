# ─────────────────────────────────────────────────────────────────────
#  Example 06 — Spin in Place
#  Category  : Movement / 2WD
#  Level     : Beginner
#
#  The robot spins a full 360 degrees in place, first right,
#  then left. Good for testing that both motors are working
#  and that your wheelbase measurement is accurate.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors2WD(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(50)

# Spin right 360 degrees
titan.turnDegrees('right', 360, True)
time.sleep(0.5)

# Spin left 360 degrees back to start
titan.turnDegrees('left', 360, True)

titan.stopMoving()

titan.End()
