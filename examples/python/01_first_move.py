# ─────────────────────────────────────────────────────────────────────
#  Example 01 — First Move
#  Category  : Movement / 2WD
#  Level     : Beginner
#
#  Your very first robot movement!
#  The robot drives forward for 30 cm, then stops.
#
#  Before running:
#    • Make sure your robot is on the floor with space ahead
#    • Check that Left Motor = 1 and Right Motor = 2
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

# Set up the robot — tell it which motors are left and right,
# and the size of the wheels and the distance between them
titan.setMovementMotors2WD(1, 2)        # Left motor=1, Right motor=2
titan.setMovementWheelDiameter(80)      # Wheel diameter in mm
titan.setMovementWheelbase(185)         # Distance between wheels in mm

# Set how fast the robot moves (0–100%)
titan.setMovementSpeed(50)

# Drive forward 30 cm, then wait until it arrives before continuing
titan.moveForDistance(30, 'cm', True)

# Stop the motors
titan.stopMoving()

titan.End()
