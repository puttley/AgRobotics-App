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
import titan
import time

titan.Begin()

titan.setMovementMotors(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(50)

for side in range(4):
    titan.moveForward(30, 'cm', True)
    titan.imuTurn('right', 90, 1)

titan.stopMoving()

titan.End()
