# ─────────────────────────────────────────────────────────────────────
#  Example 27 — Button Press Detection
#  Category  : Buttons, Pixels & Sound
#  Level     : Beginner
#
#  Prints a message to the console whenever a button is pressed.
#  The robot has four buttons: A, B, C, and D.
#  Watch the console and press each button to see it detected!
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

print('Press buttons A, B, C, or D — watch the console!')
print('')

while True:
    if titan.getButtonStatus('a'):
        print('Button A pressed!')
    if titan.getButtonStatus('b'):
        print('Button B pressed!')
    if titan.getButtonStatus('c'):
        print('Button C pressed!')
    if titan.getButtonStatus('d'):
        print('Button D pressed!')
    time.sleep(0.05)

titan.End()
