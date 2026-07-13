# ─────────────────────────────────────────────────────────────────────
#  Example 014 — Speed Ramp
#  Category  : Movement / 4WD
#  Level     : Intermediate
#
#  The robot gradually increases speed from 20% to 80% in steps
#  of 10%, then ramps back down to a stop.
#  Uses a for loop with range() to step through speed values cleanly.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors4WD(1, 2, 3, 4)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)

# Ramp up from 20% to 80% in steps of 10%
for speed in range(20, 81, 10):
    titan.setMovementSpeed(speed)
    titan.startMoving('forward')
    print('Speed:', speed, '%')
    time.sleep(0.4)

# Hold top speed briefly
time.sleep(1.0)

# Ramp back down from 80% to 20% in steps of 10%
for speed in range(80, 19, -10):
    titan.setMovementSpeed(speed)
    titan.startMoving('forward')
    print('Speed:', speed, '%')
    time.sleep(0.4)

titan.stopMoving()

titan.End()
