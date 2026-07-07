# ─────────────────────────────────────────────────────────────────────
#  Example 23 — Single Motor Run and Stop
#  Category  : Motors & Servos
#  Level     : Beginner
#
#  Runs motor 1 at 75% speed for 2 seconds, then stops it.
#  Use this to test individual motors and verify wiring.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

print('Running motor 1 at 75% for 2 seconds...')
ag.setMotorSpeed(1, 75)
time.sleep(2)

print('Stopping motor 1')
ag.setMotorStop(1, 'brake')

ag.End()
