# ─────────────────────────────────────────────────────────────────────
#  Example 06 — Spin in Place
#  Category  : Movement / 2WD
#  Level     : Beginner
#
#  The robot spins a full 360 degrees in place, first right,
#  then left. Good for testing that both motors are working
#  and that your wheelbase measurement is accurate.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(50)

# Spin right 360 degrees
ag.turnDegrees('right', 360, True)
time.sleep(0.5)

# Spin left 360 degrees back to start
ag.turnDegrees('left', 360, True)

ag.stopMoving()

ag.End()
