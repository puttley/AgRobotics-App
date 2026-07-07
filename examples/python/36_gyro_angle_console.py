# ─────────────────────────────────────────────────────────────────────
#  Example 36 — Gyro Angle — Print to Console
#  Category  : Sensors
#  Level     : Beginner
#  Hardware  : Grove 6-Axis IMU (SKU 105020012) on sensor port 1
#
#  Prints the accumulated gyro angle to the console every 100ms.
#  This is the value that imuTurn() uses internally to measure
#  how far the robot has rotated.
#
#  Try this:
#    1. Run the program and watch the console
#    2. Rotate the sensor (or robot) to the right — angle increases
#    3. Rotate to the left — angle decreases
#    4. Press Reset Angle any time to zero it back out
#
#  Positive angle = clockwise (right)
#  Negative angle = counterclockwise (left)
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

print('Gyro Angle Monitor')
print('Rotate the robot and watch the angle change')
print('Positive = clockwise   Negative = counterclockwise')
print('')

# Zero the angle accumulator before reading
ag.resetIMUAngle(1)

while True:
    angle = ag.getIMUAngle(1)
    print('Angle: {:.1f} degrees'.format(angle))
    time.sleep(0.1)

ag.End()
