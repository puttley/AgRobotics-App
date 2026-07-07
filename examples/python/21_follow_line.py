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
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(35)

print('Line follower running — place robot on a dark line')

while True:
    on_line = ag.getLineSensor(1)
    if on_line:
        # On the line — drive straight
        ag.startMoving('forward')
        ag.setSteeringControl(0)
    else:
        # Off the line — turn right to find it
        ag.setSteeringControl(50)
    time.sleep(0.02)

ag.End()
