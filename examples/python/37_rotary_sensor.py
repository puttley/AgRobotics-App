# ─────────────────────────────────────────────────────────────────────
#  Example 39 — Rotary Angle Sensor
#  Category  : Sensors
#  Level     : Beginner
#
#  Reads the rotary potentiometer (knob) and prints the angle
#  to the console in a forever loop.
#  Plug the rotary sensor into sensor port 1.
#  Turn the knob and watch the value change — range is 0 to 300 degrees.
#
#  Note: Ports 1–4 only. Port 5 does not support analog input.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

print('Rotary Angle Sensor — turn the knob and watch the value change')
print('Range: 0 to 300 degrees')
print('')

while True:
    angle = titan.getRotarySensor(1)
    print('Angle:', angle, 'degrees')
    time.sleep(0.2)

titan.End()
