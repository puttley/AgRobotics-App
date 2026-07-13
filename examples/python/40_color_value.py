# ─────────────────────────────────────────────────────────────────────
#  Example 41 — Color Value Sensor
#  Category  : Sensors
#  Level     : Beginner
#
#  Reads a numeric color index from the color sensor and prints
#  the value and its name to the console.
#  Plug the color sensor into sensor port 1.
#
#  Color index values:
#    0 = Black    1 = Red     2 = Green
#    3 = Blue     4 = White  -1 = None / Uncertain
#
#  Use this when you need a numeric value to compare in a condition
#  rather than a color name string.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

COLOR_NAMES = {0: 'Black', 1: 'Red', 2: 'Green', 3: 'Blue', 4: 'White', -1: 'None'}

print('Color Value Sensor — hold colored objects in front of the sensor')
print('Returns: 0=Black  1=Red  2=Green  3=Blue  4=White  -1=None')
print('')

while True:
    value = titan.getColorValue(1)
    name  = COLOR_NAMES.get(value, 'Unknown')
    print('Color Value:', value, ' (', name, ')')
    time.sleep(0.3)

titan.End()
