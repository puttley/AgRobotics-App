# ─────────────────────────────────────────────────────────────────────
#  Example 05 — Figure-8
#  Category  : Movement / 2WD
#  Level     : Intermediate
#
#  The robot drives a figure-8 pattern by completing one circle
#  to the right, then one circle to the left.
#  Uses steering control for smooth arcing turns.
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

ag.setMovementMotors(1, 2)
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(40)

# First loop — steer right
ag.startMoving('forward')
ag.setSteeringControl(60)      # positive = steer right
time.sleep(4.5)                # adjust time to complete one loop

# Second loop — steer left
ag.setSteeringControl(-60)     # negative = steer left
time.sleep(4.5)

ag.stopMoving()

ag.End()
