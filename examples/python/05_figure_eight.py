# ─────────────────────────────────────────────────────────────────────
#  Example 05 — Figure-8
#  Category  : Movement / 2WD
#  Level     : Intermediate
#
#  The robot drives a figure-8 pattern by completing one circle
#  to the right, then one circle to the left.
#  Uses steering control for smooth arcing turns.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

titan.setMovementMotors(1, 2)
titan.setMovementWheelDiameter(80)
titan.setMovementWheelbase(185)
titan.setMovementSpeed(40)

# First loop — steer right
titan.startMoving('forward')
titan.setSteeringControl(60)      # positive = steer right
time.sleep(4.5)                # adjust time to complete one loop

# Second loop — steer left
titan.setSteeringControl(-60)     # negative = steer left
time.sleep(4.5)

titan.stopMoving()

titan.End()
