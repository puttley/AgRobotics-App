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
import ag
import time

ag.Begin()

# ── Robot Configuration ───────────────────────────────────────────────
ag.setMovementMotors(1, 2)        # Left motor=1, Right motor=2
ag.setMovementWheelDiameter(80)   # Wheel diameter in mm
ag.setMovementWheelbase(185)      # Distance between wheels in mm
ag.setMovementSpeed(50)           # Starting speed (0–100%)

# Ready signal — green pixels and a beep
ag.setPixelColor('ABCD', '#00cc00', 30)
ag.setTone(880, 0.1)
time.sleep(0.3)
ag.setPixelOff('ABCD')

# ── Your Competition Code Below ───────────────────────────────────────
# Add your ag.moveForward(), ag.imuTurn(), ag.getTOFSensor() calls here



# ── End ───────────────────────────────────────────────────────────────
ag.setTone(440, 0.3)   # done beep
ag.End()
