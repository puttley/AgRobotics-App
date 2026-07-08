# ─────────────────────────────────────────────────────────────────────
#  Example 28 — Pixel Colors
#  Category  : Buttons, Pixels & Sound
#  Level     : Beginner
#
#  Cycles through different colors on the four NeoPixels (A, B, C, D).
#  Each pixel can display any RGB color you choose.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

# Turn all pixels red
titan.setPixelColor('ABCD', '#ff0000', 30)
time.sleep(1)

# Turn all pixels green
titan.setPixelColor('ABCD', '#00ff00', 30)
time.sleep(1)

# Turn all pixels blue
titan.setPixelColor('ABCD', '#0000ff', 30)
time.sleep(1)

# Each pixel a different color
titan.setPixelColor('A', '#ff0000', 30)   # Red
titan.setPixelColor('B', '#00ff00', 30)   # Green
titan.setPixelColor('C', '#0000ff', 30)   # Blue
titan.setPixelColor('D', '#ffcc00', 30)   # Yellow
time.sleep(2)

# Turn all off
titan.setPixelOff('ABCD')

titan.End()
