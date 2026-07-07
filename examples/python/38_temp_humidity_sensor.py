# ─────────────────────────────────────────────────────────────────────
#  Example 38 — Temperature & Humidity Sensor
#  Category  : Sensors
#  Level     : Beginner
#  Hardware  : DHT11 Temperature & Humidity Sensor on sensor port 1
#
#  Reads temperature and humidity from the DHT11 sensor and
#  prints both values to the console every 2 seconds.
#
#  Note: The DHT11 updates its reading about once per second.
#  Reading faster than that returns the same cached value.
#
#  Temperature is shown in both Celsius and Fahrenheit.
#  Humidity is shown as a percentage (0–100%).
# ─────────────────────────────────────────────────────────────────────
import ag
import time

ag.Begin()

print('Temperature & Humidity Sensor (DHT11)')
print('Plug sensor into sensor port 1')
print('')

while True:
    temp_c = ag.getTHSensor(1, 'temp', 'c')
    temp_f = ag.getTHSensor(1, 'temp', 'f')
    humid  = ag.getTHSensor(1, 'humid')

    print('Temperature: {}°C  /  {}°F'.format(temp_c, temp_f))
    print('Humidity   : {}%'.format(humid))
    print('')

    time.sleep(2.0)   # DHT11 needs ~1s between readings; 2s gives comfortable margin

ag.End()
