# ─────────────────────────────────────────────────────────────────────
#  Example 25 — Servo Sweep
#  Category  : Motors & Servos
#  Level     : Beginner
#
#  Sweeps a servo motor back and forth between 0 and 180 degrees.
#  Connect a servo to servo port 1.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

print('Servo sweep — 0 to 180 degrees and back')

# Sweep from 0 to 180 in steps of 10
for angle in range(0, 181, 10):
    ag.setServoPosition(1, angle)
    print('Servo angle:', angle)
    time.sleep(0.05)

time.sleep(0.5)

# Sweep back from 180 to 0
for angle in range(180, -1, -10):
    ag.setServoPosition(1, angle)
    print('Servo angle:', angle)
    time.sleep(0.05)

print('Sweep complete')

ag.End()
