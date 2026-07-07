# ─────────────────────────────────────────────────────────────────────
#  Example 26 — Servo with Movement
#  Category  : Motors & Servos
#  Level     : Intermediate
#
#  While the robot drives forward, a servo sweeps back and forth.
#  Shows how servos can operate independently of drive motors —
#  useful for attachments like a sorting gate or plow.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(40)

# Start driving forward
ag.startMoving('forward')

# Sweep servo while driving
for cycle in range(3):
    ag.setServoPosition(1, 0)
    time.sleep(0.5)
    ag.setServoPosition(1, 90)
    time.sleep(0.5)
    ag.setServoPosition(1, 180)
    time.sleep(0.5)
    ag.setServoPosition(1, 90)
    time.sleep(0.5)

ag.stopMoving()
ag.setServoPosition(1, 90)   # center servo

ag.End()
