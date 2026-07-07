# ─────────────────────────────────────────────────────────────────────
#  Example 29 — Sound Tones
#  Category  : Buttons, Pixels & Sound
#  Level     : Beginner
#
#  Plays a simple melody using the piezo buzzer.
#  Each note is defined by its frequency (Hz) and duration (seconds).
#  This plays a basic do-re-mi scale!
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

# Note frequencies for a C major scale
notes = [
    (262, 0.3),   # C4  — Do
    (294, 0.3),   # D4  — Re
    (330, 0.3),   # E4  — Mi
    (349, 0.3),   # F4  — Fa
    (392, 0.3),   # G4  — Sol
    (440, 0.3),   # A4  — La
    (494, 0.3),   # B4  — Ti
    (523, 0.5),   # C5  — Do (high)
]

print('Playing do-re-mi scale...')

for freq, dur in notes:
    ag.setTone(freq, dur)
    time.sleep(0.05)   # brief gap between notes

print('Done!')

ag.End()
