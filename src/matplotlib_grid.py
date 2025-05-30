import numpy as np
import time
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from sun_math import sun_position, is_daytime

# Get current UTC timestamp
utc_now = time.time()

# Calculate sun position
delta, lambda_s = sun_position(utc_now)

# Create latitude and longitude grid (1° spacing)
lat_grid = np.radians(np.linspace(-90, 90, 16))
lon_grid = np.linspace(-180, 180, 32)
Lon, Lat = np.meshgrid(lon_grid, lat_grid)

# Classify points as day or night
day_night_mask = np.vectorize(lambda lat, lon: is_daytime(lon, lat, delta, lambda_s))(Lat, Lon)

# Convert radians to degrees for plotting
Lat_deg = np.degrees(Lat)

# Plot
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()
ax.stock_img()

# Plot day and night points
ax.scatter(Lon[day_night_mask], Lat_deg[day_night_mask], color='gold', marker='o', s=1, label='Day')
ax.scatter(Lon[~day_night_mask], Lat_deg[~day_night_mask], color='midnightblue', marker='o', s=1, label='Night')

# Format timestamp for title
timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime(utc_now))
plt.title(f'Day and Night Grid (based on Terminator) at {timestamp_str}')
plt.show()