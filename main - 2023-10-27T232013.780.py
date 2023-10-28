import random

# Mock GPS coordinates for demonstration purposes
latitude = random.uniform(40.0, 41.0)
longitude = random.uniform(-75.0, -74.0)

# Function to determine the next or last exit based on GPS location
def get_exit_info(latitude, longitude):
    # In a real-world scenario, you would use a map or GPS API to determine the nearest exit.
    # This is a simplified example using random data.
    exits = [
        {"name": "Exit A", "mile_marker": 10},
        {"name": "Exit B", "mile_marker": 15},
        {"name": "Exit C", "mile_marker": 20},
    ]

    closest_exit = min(exits, key=lambda exit: abs(exit["mile_marker"] - latitude))
    return closest_exit

# Get the closest exit information
closest_exit = get_exit_info(latitude, longitude)

# Output the result
print(f"Current GPS Coordinates: Latitude {latitude}, Longitude {longitude}")
print(f"Next Exit: {closest_exit['name']} at Mile Marker {closest_exit['mile_marker']}")

