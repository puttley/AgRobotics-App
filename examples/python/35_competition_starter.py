# ─────────────────────────────────────────────────────────────────────
#  Example 35 — Competition Starter Template
#  Category  : Templates
#  Level     : Beginner
#
#  A ready-to-use starting point for your AgRobotics competition
#  program. The robot configuration is already set up.
#  Add your movement and sensor code below the comment.
#
#  Press the SELECT button to start the program.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

# ── Robot Configuration ───────────────────────────────────────────────
titan.setMovementMotors2WD(1, 2)     # Left motor=1, Right motor=2
titan.setMovementWheelDiameter(80)   # Wheel diameter in mm
titan.setMovementWheelbase(185)      # Distance between wheels in mm
titan.setMovementSpeed(50)           # Starting speed (0–100%)

# Ready signal — green pixels and a beep
titan.setPixelColor('ABCD', '#00cc00', 30)
titan.setTone(880, 0.1)
time.sleep(0.3)
titan.setPixelOff('ABCD')

# ── Your Competition Code Below ───────────────────────────────────────
while True:  # forever loop
    # Add your titan.moveForDistance(), titan.imuTurn(), titan.getTOFSensor() calls here (remove pass after addding code)
  pass


# ── End ───────────────────────────────────────────────────────────────
titan.setTone(440, 0.3)   # done beep
titan.End()
