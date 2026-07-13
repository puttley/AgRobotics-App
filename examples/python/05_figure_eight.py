# ─────────────────────────────────────────────────────────────────────
#  Example 05 — Figure-8
#  Category  : Movement / 2WD
#  Level     : Intermediate
#
#  The robot drives a figure-8 pattern 
#  
#  Uses steering control for smooth arcing turns.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors2WD(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(40)

# First loop — steer right
titan.startMovingWithSteering(60)   # postive steer right
time.sleep(5)

# Second loop — steer left
titan.startMovingWithSteering(-60)  # negative steer left
time.sleep(13)

# Third loop — steer right
titan.startMovingWithSteering(60)   # postive steer right
time.sleep(9)

titan.stopMoving()

titan.End()
