# ─────────────────────────────────────────────────────────────────────
#  Example 24 — All Motors Check
#  Category  : Motors & Servos
#  Level     : Beginner
#
#  Runs each motor one at a time so you can verify that all four
#  motors are connected and spinning in the right direction.
#  Great for setup and troubleshooting!
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

for motor in range(1, 5):
    print('Testing motor', motor, '...')
    ag.setMotorSpeed(motor, 60)
    time.sleep(1.5)
    ag.setMotorStop(motor, 'brake')
    time.sleep(0.5)

print('All motors checked!')

ag.End()
