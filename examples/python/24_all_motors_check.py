# ─────────────────────────────────────────────────────────────────────
#  Example 24 — All Motors Check
#  Category  : Motors & Servos
#  Level     : Beginner
#
#  Runs each motor one at a time so you can verify that all four
#  motors are connected and spinning in the right direction.
#  Great for setup and troubleshooting!
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

for motor in range(1, 5):
    print('Testing motor', motor, '...')
    titan.setMotorSpeed(motor, 60)
    time.sleep(1.5)
    titan.setMotorStop(motor, 'brake')
    time.sleep(0.5)

print('All motors checked!')

titan.End()
