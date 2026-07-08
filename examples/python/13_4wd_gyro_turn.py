# ─────────────────────────────────────────────────────────────────────
#  Example 13 — 4WD Gyro Square Pattern
#  Category  : Movement / 4WD
#  Level     : Intermediate
#  Hardware  : Grove 6-Axis IMU (SKU 105020012) on sensor port 1
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors4WD(1, 2, 3, 4)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(50)

for side in range(4):
    titan.moveForward(30, 'cm', True)
    titan.imuTurn('right', 90, 1)

titan.stopMoving()

titan.End()
