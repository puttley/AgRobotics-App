# ─────────────────────────────────────────────────────────────────────
#  Example 22 — Color-Triggered Action
#  Category  : Sensors + Movement
#  Level     : Intermediate
#
#  The robot drives forward until it sees a specific color,
#  then reacts differently depending on which color it sees.
#  Red = stop, Green = turn right, Blue = turn left.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(40)

ag.startMoving('forward')
print('Driving — watching for colors...')

while True:
    color = ag.getColorName(1)

    if color == 'red':
        ag.stopMoving()
        ag.setTone(220, 0.3)
        print('Red detected — stopping!')
        break

    elif color == 'green':
        ag.turnDegrees('right', 90, True)
        ag.startMoving('forward')
        print('Green detected — turning right')

    elif color == 'blue':
        ag.turnDegrees('left', 90, True)
        ag.startMoving('forward')
        print('Blue detected — turning left')

    time.sleep(0.1)

ag.End()
