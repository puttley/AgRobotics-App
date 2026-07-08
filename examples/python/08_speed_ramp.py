# ─────────────────────────────────────────────────────────────────────
#  Example 08 — Speed Ramp
#  Category  : Movement / 2WD
#  Level     : Intermediate
#
#  The robot gradually increases speed from 20% to 80%, then
#  ramps back down to a stop. Useful for smooth acceleration
#  and understanding how setMovementSpeed works while moving.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)

# Start moving slowly
titan.setMovementSpeed(20)
titan.startMoving('forward')

# Ramp up speed in steps
for speed in range(20, 81, 10):
    titan.setMovementSpeed(speed)
    print('Speed:', speed, '%')
    time.sleep(0.4)

# Hold top speed briefly
time.sleep(1.0)

# Ramp back down
for speed in range(80, 19, -10):
    titan.setMovementSpeed(speed)
    print('Speed:', speed, '%')
    time.sleep(0.4)

titan.stopMoving()

titan.End()
