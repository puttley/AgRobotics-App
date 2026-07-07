# ─────────────────────────────────────────────────────────────────────
#  Example 28 — Pixel Colors
#  Category  : Buttons, Pixels & Sound
#  Level     : Beginner
#
#  Cycles through different colors on the four NeoPixels (A, B, C, D).
#  Each pixel can display any RGB color you choose.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

# Turn all pixels red
ag.setPixelColor('ABCD', '#ff0000', 30)
time.sleep(1)

# Turn all pixels green
ag.setPixelColor('ABCD', '#00ff00', 30)
time.sleep(1)

# Turn all pixels blue
ag.setPixelColor('ABCD', '#0000ff', 30)
time.sleep(1)

# Each pixel a different color
ag.setPixelColor('A', '#ff0000', 30)   # Red
ag.setPixelColor('B', '#00ff00', 30)   # Green
ag.setPixelColor('C', '#0000ff', 30)   # Blue
ag.setPixelColor('D', '#ffcc00', 30)   # Yellow
time.sleep(2)

# Turn all off
ag.setPixelOff('ABCD')

ag.End()
