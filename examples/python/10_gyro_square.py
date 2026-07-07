# ─────────────────────────────────────────────────────────────────────
#  Example 10 — Gyro Square Pattern
#  Category  : Movement / 2WD
#  Level     : Intermediate
#  Hardware  : Grove 6-Axis IMU (SKU 105020012) on sensor port 1
#
#  Drives a square using gyro turns instead of encoder turns.
#  On competition surfaces where wheels may slip, this produces
#  a much more accurate square than Example 04.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(50)

for side in range(4):
    ag.moveForward(30, 'cm', True)
    ag.imuTurn('right', 90, 1)

ag.stopMoving()

ag.End()
