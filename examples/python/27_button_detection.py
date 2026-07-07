# ─────────────────────────────────────────────────────────────────────
#  Example 27 — Button Press Detection
#  Category  : Buttons, Pixels & Sound
#  Level     : Beginner
#
#  Prints a message to the console whenever a button is pressed.
#  The robot has four buttons: A, B, C, and D.
#  Watch the console and press each button to see it detected!
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

print('Press buttons A, B, C, or D — watch the console!')
print('')

while True:
    if ag.getButtonStatus('a'):
        print('Button A pressed!')
    if ag.getButtonStatus('b'):
        print('Button B pressed!')
    if ag.getButtonStatus('c'):
        print('Button C pressed!')
    if ag.getButtonStatus('d'):
        print('Button D pressed!')
    time.sleep(0.05)

ag.End()
