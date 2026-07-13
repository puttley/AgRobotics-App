# ─────────────────────────────────────────────────────────────────────
#  Example 40 — Reflected Light Sensor
#  Category  : Sensors
#  Level     : Beginner
#
#  Reads the reflected light intensity from the color sensor and
#  prints the value to the console in a forever loop.
#  Plug the color sensor into sensor port 1.
#
#  Range: 0–100
#  High value = bright or white surface
#  Low value  = dark or black surface
#
#  This is the key sensor for line following!
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

print('Reflected Light Sensor')
print('High = bright/white surface   Low = dark/black surface')
print('')

while True:
    light = titan.getReflectedLight(1)
    print('Reflected Light:', light)
    time.sleep(0.2)

titan.End()
