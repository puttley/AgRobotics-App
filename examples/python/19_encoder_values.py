# ─────────────────────────────────────────────────────────────────────
#  Example 19 — Encoder Values
#  Category  : Sensors
#  Level     : Beginner
#
#  Prints encoder counts for motors 1 and 2 to the console.
#  Encoders measure how far each motor has turned.
#
#  Try this two ways:
#    1. Let the robot drive forward and watch the counts increase
#    2. Pick the robot up, spin each wheel by hand, and watch the
#       encoder counts change in real time
#
#  Encoder counts increase as the motor turns forward,
#  and decrease when it turns backward.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

# Reset both encoders to zero before reading
titan.resetEncoder(1)
titan.resetEncoder(2)

print('Encoder Values — spin the wheels by hand or let the robot drive')
print('Motor 1 = Left,  Motor 2 = Right')
print('')

while True:
    enc1 = titan.getEncoder(1)
    enc2 = titan.getEncoder(2)
    print('Motor 1:', enc1, '  Motor 2:', enc2)
    time.sleep(0.2)

titan.End()
