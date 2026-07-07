# ─────────────────────────────────────────────────────────────────────
#  Example 08 — Speed Ramp
#  Category  : Movement / 2WD
#  Level     : Intermediate
#
#  The robot gradually increases speed from 20% to 80%, then
#  ramps back down to a stop. Useful for smooth acceleration
#  and understanding how setMovementSpeed works while moving.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)

# Start moving slowly
ag.setMovementSpeed(20)
ag.startMoving('forward')

# Ramp up speed in steps
for speed in range(20, 81, 10):
    ag.setMovementSpeed(speed)
    print('Speed:', speed, '%')
    time.sleep(0.4)

# Hold top speed briefly
time.sleep(1.0)

# Ramp back down
for speed in range(80, 19, -10):
    ag.setMovementSpeed(speed)
    print('Speed:', speed, '%')
    time.sleep(0.4)

ag.stopMoving()

ag.End()
