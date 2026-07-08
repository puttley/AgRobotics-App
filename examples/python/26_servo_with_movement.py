# ─────────────────────────────────────────────────────────────────────
#  Example 26 — Servo with Movement
#  Category  : Motors & Servos
#  Level     : Intermediate
#
#  While the robot drives forward, a servo sweeps back and forth.
#  Shows how servos can operate independently of drive motors —
#  useful for attachments like a sorting gate or plow.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(40)

# Start driving forward
titan.startMoving('forward')

# Sweep servo while driving
for cycle in range(3):
    titan.setServoPosition(1, 0)
    time.sleep(0.5)
    titan.setServoPosition(1, 90)
    time.sleep(0.5)
    titan.setServoPosition(1, 180)
    time.sleep(0.5)
    titan.setServoPosition(1, 90)
    time.sleep(0.5)

titan.stopMoving()
titan.setServoPosition(1, 90)   # center servo

titan.End()
