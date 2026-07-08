# ─────────────────────────────────────────────────────────────────────
#  Example 07 — Steering Control
#  Category  : Movement / 2WD
#  Level     : Intermediate
#
#  Shows how to use the steering block to make smooth arcing turns
#  instead of sharp pivot turns. Steering value ranges from
#  -100 (hard left) to 0 (straight) to +100 (hard right).
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(50)

# Drive straight
titan.startMoving('forward')
titan.setSteeringControl(0)
time.sleep(1.5)

# Gentle right arc
titan.setSteeringControl(30)
time.sleep(1.5)

# Straight again
titan.setSteeringControl(0)
time.sleep(1.5)

# Gentle left arc
titan.setSteeringControl(-30)
time.sleep(1.5)

titan.stopMoving()

titan.End()
