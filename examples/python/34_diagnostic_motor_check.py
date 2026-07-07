# ─────────────────────────────────────────────────────────────────────
#  Example 34 — Diagnostic: Motor Check
#  Category  : Diagnostics
#  Level     : Beginner
#
#  Tests each motor one at a time and reads the encoder value
#  so you can confirm direction and encoder counts are correct.
#  Run this before competition to verify all motors are healthy.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

print('=== Motor Diagnostic ===')
print('Each motor will run for 1.5 seconds')
print('Check that it spins in the FORWARD direction')
print('')

for motor in range(1, 5):
    ag.resetEncoder(motor)
    print('Motor', motor, '— running forward...')
    ag.setMotorSpeed(motor, 60)
    time.sleep(1.5)
    ag.setMotorStop(motor, 'brake')
    enc = ag.getEncoder(motor)
    print('  Encoder count after forward run:', enc)
    if enc > 0:
        print('  Direction: OK')
    else:
        print('  Direction: REVERSED — swap motor wires or check port')
    print('')
    time.sleep(0.5)

print('Motor check complete!')

ag.End()
