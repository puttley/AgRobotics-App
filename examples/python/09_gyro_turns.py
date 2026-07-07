# ─────────────────────────────────────────────────────────────────────
#  Example 09 — Gyro Turns
#  Category  : Movement / 2WD
#  Level     : Intermediate
#  Hardware  : Grove 6-Axis IMU (SKU 105020012) on sensor port 1
#
#  Uses the gyro sensor for accurate turns — much more precise
#  than encoder-based turns on slippery or dusty surfaces.
#  Demonstrates 90°, 180°, and 360° gyro turns.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(50)

# 90-degree right turn using gyro
print('Gyro turn: 90 right')
ag.imuTurn('right', 90, 1)
time.sleep(0.5)

# 90-degree left turn using gyro
print('Gyro turn: 90 left')
ag.imuTurn('left', 90, 1)
time.sleep(0.5)

# 180-degree turn
print('Gyro turn: 180')
ag.imuTurn('right', 180, 1)
time.sleep(0.5)

# Full 360-degree spin
print('Gyro turn: 360')
ag.imuTurn('right', 360, 1)

ag.End()
