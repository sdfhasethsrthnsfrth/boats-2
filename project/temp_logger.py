#!/usr/bin/python3
import subprocess
from datetime import datetime

# Define log file paths
log_temp_timestamp = '/home/Captain/project/temperaturelog/cpu_temp_log_with_timestamp.txt'
log_temp_numerical = '/home/Captain/project/temperaturelog/cpu_temp_log_numerical_only.txt'

def get_cpu_temp():
    # Get only the numeric part of the CPU temperature.
    result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
    temp_output = result.stdout.strip()
    temp_value = temp_output.split('=')[1].replace("'C", "")  # Extract just the temperature number
    return temp_value

# Function to log temperature
def log_temperature():
    temp = get_cpu_temp()

    # Log with timestamp
    with open(log_temp_timestamp, 'a') as f_with_timestamp:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f_with_timestamp.write(f"{timestamp} - {temp}\n")
    
    # Log only the temperature value
    with open(log_temp_numerical, 'a') as f_numerical_only:
        f_numerical_only.write(f"{temp}\n")

# Execute logging
log_temperature()
