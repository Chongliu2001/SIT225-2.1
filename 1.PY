import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

ser = serial.Serial('COM3', 9600) 

# Generate a datetime range for 30 minutes with a 30 seconds interval
time_index = pd.date_range(start=datetime.datetime.now(), periods=60, freq='30S')

# Simulate temperature and humidity data
# Assume initial temperature is 22.0 degrees Celsius and initial humidity is 50.0%
# Temperature increases slowly by 1 degree every 30 minutes (0.033 degrees every 30 seconds)
# Humidity fluctuates slightly within 0.5% range

temperature = 22.0 + np.arange(0, 60) * (1 / 60)
humidity = 50.0 + np.sin(np.arange(0, 60) / 10) * 0.5

# Create a DataFrame
data = pd.DataFrame({
    'timestamp': time_index.strftime('%Y%m%d%H%M%S'),
    'temperature': np.round(temperature, 2),
    'humidity': np.round(humidity, 2)
})

# Save to CSV
data.to_csv('/mnt/data/sensor_data_corrected.csv', index=False)

# Read the data from CSV file
data = pd.read_csv('/mnt/data/sensor_data_corrected.csv')

# Convert timestamp to datetime format
data['timestamp'] = pd.to_datetime(data['timestamp'], format='%Y%m%d%H%M%S')

# Plot the data
plt.figure(figsize=(12, 6)) # Set the figure size
plt.plot(data['timestamp'], data['temperature'], label='Temperature (°C)', color='tab:red') # Plot temperature
plt.plot(data['timestamp'], data['humidity'], label='Humidity (%)', color='tab:blue') # Plot humidity

# Adding titles and labels
plt.title('Temperature and Humidity Over Time') # Set the title of the plot
plt.xlabel('Timestamp') # Set the x-axis label
plt.ylabel('Value') # Set the y-axis label
plt.legend() # Add legend to the plot
plt.grid(True) # Add grid lines

# Save the plot
plt.savefig('/mnt/data/sensor_data_plot.png') # Save the plot as a PNG file

# Display the plot
plt.show() # Show the plot
