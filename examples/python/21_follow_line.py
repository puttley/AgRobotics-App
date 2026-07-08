# ─────────────────────────────────────────────────────────────────────
#  Example 21 — Follow Line
#  Category  : Sensors + Movement
#  Level     : Intermediate
#
#  The robot follows a dark line on a light surface.
#  Uses one line sensor on port 1.
#  When on the line, drive forward.
#  When off the line, turn to find it again.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(35)

print('Line follower running — place robot on a dark line')

while True:
    on_line = titan.getLineSensor(1)
    if on_line:
        # On the line — drive straight
        titan.startMoving('forward')
        titan.setSteeringControl(0)
    else:
        # Off the line — turn right to find it
        titan.setSteeringControl(50)
    time.sleep(0.02)

titan.End()
