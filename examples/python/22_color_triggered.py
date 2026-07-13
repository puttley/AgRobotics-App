# ─────────────────────────────────────────────────────────────────────
#  Example 22 — Color-Triggered Action
#  Category  : Sensors + Movement
#  Level     : Intermediate
#
#  The robot drives forward until it sees a specific color,
#  then reacts differently depending on which color it sees.
#  Red = stop, Green = turn right, Blue = turn left.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors2WD(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(40)

titan.startMoving('forward')
print('Driving — watching for colors...')

while True:
    color = titan.getColorName(1)

    if color == 'red':
        titan.stopMoving()
        titan.setTone(220, 0.3)
        print('Red detected — stopping!')
        break

    elif color == 'green':
        titan.turnDegrees('right', 90, True)
        titan.startMoving('forward')
        print('Green detected — turning right')

    elif color == 'blue':
        titan.turnDegrees('left', 90, True)
        titan.startMoving('forward')
        print('Blue detected — turning left')

    time.sleep(0.1)

titan.End()
