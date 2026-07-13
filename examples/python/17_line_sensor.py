# ─────────────────────────────────────────────────────────────────────
#  Example 17 — Line Sensor
#  Category  : Sensors
#  Level     : Beginner
#
#  Reads the line sensor and prints the value to the console.
#  Returns True (1) when reflected light is detected, False (0) otherwise (dark line)
#  Plug the sensor into sensor port 1.
#  Try holding the sensor over a dark line on white paper!
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

print('Line Sensor — True = line detected, False = no line')
print('')

while True:
    on_line = titan.getLineSensor(1)
    print('Status:', on_line)
    time.sleep(0.2)

titan.End()
