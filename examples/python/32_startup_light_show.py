# ─────────────────────────────────────────────────────────────────────
#  Example 32 — Startup Light Show
#  Category  : Buttons, Pixels & Sound
#  Level     : Beginner
#
#  A fun startup animation — pixels chase around in a pattern
#  while a little fanfare plays. Good for competition day!
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

# Fanfare tones
fanfare = [(523, 0.1), (659, 0.1), (784, 0.1), (1047, 0.3)]
for freq, dur in fanfare:
    titan.setTone(freq, dur)
    time.sleep(0.02)

# Chase animation — each pixel lights up in sequence
colors = ['#ff0000', '#00cc00', '#0044ff', '#ccaa00']
pixels = ['A', 'B', 'C', 'D']

for _ in range(3):
    for i in range(4):
        titan.setPixelOff('ABCD')
        titan.setPixelColor(pixels[i], colors[i], 60)
        time.sleep(0.12)

# All on together
for i in range(4):
    titan.setPixelColor(pixels[i], colors[i], 40)
time.sleep(1.0)

# Fade out
for brightness in range(40, 0, -5):
    for i in range(4):
        titan.setPixelColor(pixels[i], colors[i], brightness)
    time.sleep(0.08)

titan.setPixelOff('ABCD')
print('Ready!')

titan.End()
