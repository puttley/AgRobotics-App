# ─────────────────────────────────────────────────────────────────────
#  Example 30 — Buttons + Pixels + Sound Together
#  Category  : Buttons, Pixels & Sound
#  Level     : Intermediate
#
#  Each button lights up a different pixel color and plays a tone.
#  Press A, B, C, or D to see and hear the response.
#  Press all four to exit.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setPixelOff('ABCD')
print('Press A, B, C, or D')

while True:
    if ag.getButtonStatus('a'):
        ag.setPixelOff('ABCD')
        ag.setPixelColor('A', '#ff0000', 50)
        ag.setTone(440, 0.15)
        print('A — Red')
        time.sleep(0.3)

    elif ag.getButtonStatus('b'):
        ag.setPixelOff('ABCD')
        ag.setPixelColor('B', '#00cc00', 50)
        ag.setTone(550, 0.15)
        print('B — Green')
        time.sleep(0.3)

    elif ag.getButtonStatus('c'):
        ag.setPixelOff('ABCD')
        ag.setPixelColor('C', '#0044ff', 50)
        ag.setTone(660, 0.15)
        print('C — Blue')
        time.sleep(0.3)

    elif ag.getButtonStatus('d'):
        ag.setPixelOff('ABCD')
        ag.setPixelColor('D', '#ccaa00', 50)
        ag.setTone(880, 0.15)
        print('D — Yellow')
        time.sleep(0.3)

    time.sleep(0.02)

ag.End()
