# ─────────────────────────────────────────────────────────────────────
#  Example 07 — Steering Control
#  Category  : Movement / 2WD
#  Level     : Intermediate
#
#  Shows how to use the steering block to make smooth arcing turns
#  instead of sharp pivot turns. Steering value ranges from
#  -100 (hard left) to 0 (straight) to +100 (hard right).
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(50)

# Drive straight
ag.startMoving('forward')
ag.setSteeringControl(0)
time.sleep(1.5)

# Gentle right arc
ag.setSteeringControl(30)
time.sleep(1.5)

# Straight again
ag.setSteeringControl(0)
time.sleep(1.5)

# Gentle left arc
ag.setSteeringControl(-30)
time.sleep(1.5)

ag.stopMoving()

ag.End()
