# ─────────────────────────────────────────────────────────────────────
#  Example 33 — Diagnostic: Sensor Check
#  Category  : Diagnostics
#  Level     : Beginner
#
#  Reads all sensor ports and prints values to the console.
#  Use this on setup day to confirm each sensor is connected
#  and returning reasonable values before your competition run.
#
#  Connect sensors to ports 1–5 and run this program.
# ─────────────────────────────────────────────────────────────────────
import titan
import time

titan.Begin()

print('=== Sensor Diagnostic ===')
print('Reading all sensor ports — check each one is responding')
print('')

while True:
    print('--- Port readings ---')
    for port in range(1, 6):
        try:
            tof  = titan.getTOFSensor(port)
            print('  Port', port, '| TOF:', tof, 'mm')
        except:
            print('  Port', port, '| TOF: not detected')
    print('')
    time.sleep(1.0)

titan.End()
