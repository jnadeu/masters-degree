# temp_dashboard.py
import redis as rd

# Connect to Redis
r = rd.Redis(host='localhost', port=6379, decode_responses=True)

# Create a Redis pub/sub object
p = r.pubsub()

# Subscribe to all temperature update channels
p.psubscribe('temp_updates:*')

# Store the last temperature for each city
last_temperatures = {}

def handle_message(message):
    """Process the temperature message"""
    channel = message['channel']
    # Extract the city from the channel name
    city = channel.split(":")[1]
    current_temp = float(message['data'])
    
    if city in last_temperatures:
        last_temp = last_temperatures[city]
        temp_diff = current_temp - last_temp
        print(f"{city} - Current temperature: {current_temp}°C, Change: {temp_diff:+.2f}°C")
    else:
        print(f"{city} - Current temperature: {current_temp}°C (First reading)")
    
    last_temperatures[city] = current_temp

# Listen for new messages on the subscribed channels
print("Listening for temperature updates...")
for message in p.listen():
    # Check if the message is a pattern message
    if message['type'] == 'pmessage':
        handle_message(message)
