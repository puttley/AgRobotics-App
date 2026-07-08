# ─────────────────────────────────────────────────────────────────────
#  Example 23 — Single Motor Run and Stop
#  Category  : Motors & Servos
#  Level     : Beginner
#
#  Runs motor 1 at 75% speed for 2 seconds, then stops it.
#  Use this to test individual motors and verify wiring.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

print('Running motor 1 at 75% for 2 seconds...')
titan.setMotorSpeed(1, 75)
time.sleep(2)

print('Stopping motor 1')
titan.setMotorStop(1, 'brake')

titan.End()
