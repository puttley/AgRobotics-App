# ─────────────────────────────────────────────────────────────────────
#  Example 17 — Line Sensor
#  Category  : Sensors
#  Level     : Beginner
#
#  Reads the line sensor and prints the value to the console.
#  Returns True when a dark line is detected, False otherwise.
#  Plug the sensor into sensor port 1.
#  Try holding the sensor over a dark line on white paper!
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

print('Line Sensor — True = line detected, False = no line')
print('')

while True:
    on_line = ag.getLineSensor(1)
    print('On line:', on_line)
    time.sleep(0.2)

ag.End()
