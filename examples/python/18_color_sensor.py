# ─────────────────────────────────────────────────────────────────────
#  Example 18 — Color Sensor
#  Category  : Sensors
#  Level     : Beginner
#
#  Reads the color sensor and prints the detected color name.
#  Plug the sensor into sensor port 1.
#  Try holding colored cards in front of the sensor!
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

print('Color Sensor — hold colored objects in front of the sensor')
print('')

while True:
    color = ag.getColorName(1)
    print('Color detected:', color)
    time.sleep(0.3)

ag.End()
