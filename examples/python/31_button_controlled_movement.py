# ─────────────────────────────────────────────────────────────────────
#  Example 31 — Button-Controlled Movement
#  Category  : Buttons, Pixels & Sound + Movement
#  Level     : Intermediate
#
#  Use the buttons to control the robot manually:
#    A = Forward    B = Backward
#    C = Turn Left  D = Turn Right
#  Release all buttons to stop.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(50)

print('Button control:  A=Forward  B=Backward  C=Left  D=Right')

moving = False

while True:
    a = ag.getButtonStatus('a')
    b = ag.getButtonStatus('b')
    c = ag.getButtonStatus('c')
    d = ag.getButtonStatus('d')

    if a:
        ag.startMoving('forward')
        ag.setPixelColor('A', '#00ff00', 30)
        moving = True
    elif b:
        ag.startMoving('backward')
        ag.setPixelColor('B', '#ffcc00', 30)
        moving = True
    elif c:
        ag.startMoving('forward')
        ag.setSteeringControl(-70)
        ag.setPixelColor('C', '#0044ff', 30)
        moving = True
    elif d:
        ag.startMoving('forward')
        ag.setSteeringControl(70)
        ag.setPixelColor('D', '#ff0000', 30)
        moving = True
    else:
        if moving:
            ag.stopMoving()
            ag.setSteeringControl(0)
            ag.setPixelOff('ABCD')
            moving = False

    time.sleep(0.02)

ag.End()
