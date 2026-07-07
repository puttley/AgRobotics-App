# ─────────────────────────────────────────────────────────────────────
#  Example 11 — 4WD First Move
#  Category  : Movement / 4WD
#  Level     : Beginner
#
#  Same as Example 01 but configured for a 4-wheel drive robot.
#  All four motors run together — two on each side.
#
#  Default 4WD wiring:
#    Left side  : Motors 1 and 2
#    Right side : Motors 3 and 4
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

# 4WD config — two motors per side
ag.setMovementMotors4WD(1, 2, 3, 4)   # Left1, Left2, Right1, Right2
ag.setMovementWheelDiameter(80)
ag.setMovementWheelbase(185)
ag.setMovementSpeed(50)

ag.moveForward(30, 'cm', True)
ag.stopMoving()

ag.End()
