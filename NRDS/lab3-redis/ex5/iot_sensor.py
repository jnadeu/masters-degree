# iot_sensor.py
import sys
import time
import random
import redis as rd

# Check if city is provided
if len(sys.argv) < 2:
    print("Usage: python iot_sensor.py <city>")
    sys.exit(1)

city = sys.argv[1]

# Connect to Redis
r = rd.Redis(host='localhost', port=6379, decode_responses=True)

def get_temperature():
    """Simulate temperature sensor. Random temperature between -10 and 44 ºC"""
    return round(random.uniform(-10.0, 44.0), 2)

while True:
    temperature = get_temperature()
    # Publish the temperature to the Redis channel
    r.publish(f"temp_updates:{city}", temperature)
    print(f"Published temperature {temperature}ºC for {city}")
    # Wait 30 seconds before sending the next update
    time.sleep(30) 
