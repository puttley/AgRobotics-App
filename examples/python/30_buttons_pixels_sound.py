# ─────────────────────────────────────────────────────────────────────
#  Example 30 — Buttons + Pixels + Sound Together
#  Category  : Buttons, Pixels & Sound
#  Level     : Intermediate
#
#  Each button lights up a different pixel color and plays a tone.
#  Press A, B, C, or D to see and hear the response.
#  Press all four to exit.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setPixelOff('ABCD')
print('Press A, B, C, or D')

while True:
    if titan.getButtonStatus('a'):
        titan.setPixelOff('ABCD')
        titan.setPixelColor('A', '#ff0000', 50)
        titan.setTone(440, 0.15)
        print('A — Red')
        time.sleep(0.3)

    elif titan.getButtonStatus('b'):
        titan.setPixelOff('ABCD')
        titan.setPixelColor('B', '#00cc00', 50)
        titan.setTone(550, 0.15)
        print('B — Green')
        time.sleep(0.3)

    elif titan.getButtonStatus('c'):
        titan.setPixelOff('ABCD')
        titan.setPixelColor('C', '#0044ff', 50)
        titan.setTone(660, 0.15)
        print('C — Blue')
        time.sleep(0.3)

    elif titan.getButtonStatus('d'):
        titan.setPixelOff('ABCD')
        titan.setPixelColor('D', '#ccaa00', 50)
        titan.setTone(880, 0.15)
        print('D — Yellow')
        time.sleep(0.3)

    time.sleep(0.02)

titan.End()
