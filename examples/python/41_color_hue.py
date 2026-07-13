# ─────────────────────────────────────────────────────────────────────
#  Example 42 — Color Hue Sensor
#  Category  : Sensors
#  Level     : Intermediate
#
#  Reads the hue angle from the color sensor and prints it to the
#  console. Hue encodes pure color identity (0–360 degrees) regardless
#  of how bright or dark the surface is.
#  Plug the color sensor into sensor port 1.
#
#  Approximate hue values:
#    Red    ~  0° or 360°
#    Yellow ~ 60°
#    Green  ~ 120°
#    Blue   ~ 240°
#    Returns -1 for black, white, or gray (achromatic) surfaces.
#
#  Use hue to train the robot to recognize specific color cards —
#  read the hue, store it in a variable, then compare it later.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

print('Color Hue Sensor — hold colored objects in front of the sensor')
print('Hue range: 0–360 degrees   Returns -1 for black/white/gray')
print('')

while True:
    hue = titan.getColorHue(1)
    if hue == -1:
        print('Hue: -1 (achromatic — black, white, or gray)')
    else:
        print('Hue:', hue, 'degrees')
    time.sleep(0.2)

titan.End()
