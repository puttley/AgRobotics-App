# ─────────────────────────────────────────────────────────────────────
#  Example 21 — Follow Line
#  Category  : Sensors + Movement
#  Level     : Intermediate
#
#  The robot follows the outside of a dark line on a light surface.
#  Uses one line sensor on port 1.
#  When on the line, drive steer right.
#  When off the line, steer left to find it again.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors2WD(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(35)

print('Line follower running — place robot on a dark line')

while True:
    on_line = titan.getLineSensor(1)
    if on_line:
        # On the line — steer right
        titan.startMovingWithSteering(-75)
    else:
        # Off the line — steer left
        titan.startMovingWithSteering(75)
    time.sleep(0.02)

titan.End()
