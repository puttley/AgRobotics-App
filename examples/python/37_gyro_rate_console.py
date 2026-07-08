# ─────────────────────────────────────────────────────────────────────
#  Example 37 — Gyro Turn Rate — Print to Console
#  Category  : Sensors
#  Level     : Intermediate
#  Hardware  : Grove 6-Axis IMU (SKU 105020012) on sensor port 1
#
#  Calculates and prints how fast the robot is turning in
#  degrees per second by measuring how much the angle changes
#  between readings.
#
#  Understanding rate vs angle:
#    Angle = total degrees rotated since reset (where am I pointing?)
#    Rate  = how fast I am rotating right now (deg/s)
#
#  Try this:
#    • Sit still — rate near zero, angle unchanged
#    • Spin slowly — small rate, angle grows slowly
#    • Spin fast — large rate, angle grows quickly
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

print('Gyro Turn Rate Monitor')
print('Angle = total degrees rotated since reset')
print('Rate  = how fast rotating right now (deg/s)')
print('')

titan.resetIMUAngle(1)

prev_angle = 0.0
prev_time  = time.ticks_ms()

while True:
    angle     = titan.getIMUAngle(1)
    now       = time.ticks_ms()
    elapsed_s = time.ticks_diff(now, prev_time) / 1000.0

    if elapsed_s > 0:
        rate = (angle - prev_angle) / elapsed_s
    else:
        rate = 0.0

    print('Angle: {:6.1f} deg   Rate: {:7.1f} deg/s'.format(angle, rate))

    prev_angle = angle
    prev_time  = now
    time.sleep(0.1)

titan.End()
