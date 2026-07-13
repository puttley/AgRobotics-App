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
import titan
import time

titan.Begin()

titan.setMovementMotors2WD(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(50)

print('Button control:  A=Forward  B=Backward  C=Left  D=Right')

moving = False

while True:
    a = titan.getButtonStatus('a')
    b = titan.getButtonStatus('b')
    c = titan.getButtonStatus('c')
    d = titan.getButtonStatus('d')

    if a:
        titan.startMoving('forward')
        titan.setPixelColor('A', '#00ff00', 30)
        moving = True
    elif c:
        titan.startMoving('backward')
        titan.setPixelColor('B', '#ffcc00', 30)
        moving = True
    elif d:
        titan.startMovingWithSteering(-70)
        titan.setPixelColor('C', '#0044ff', 30)
        moving = True
    elif b:
        titan.startMovingWithSteering(70)
        titan.setPixelColor('D', '#ff0000', 30)
        moving = True
    else:
        if moving:
            titan.stopMoving()
            titan.setPixelOff('ABCD')
            moving = False

    time.sleep(0.02)

titan.End()
