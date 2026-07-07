# ─────────────────────────────────────────────────────────────────────
#  Example 13 — 4WD Gyro Square Pattern
#  Category  : Movement / 4WD
#  Level     : Intermediate
#  Hardware  : Grove 6-Axis IMU (SKU 105020012) on sensor port 1
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors4WD(1, 2, 3, 4)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(50)

for side in range(4):
    ag.moveForward(30, 'cm', True)
    ag.imuTurn('right', 90, 1)

ag.stopMoving()

ag.End()
