import numpy as np
import math
import time
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def sun_position(utc_timestamp):
    """
    Calculates the solar declination and subsolar longitude for a given UTC timestamp.
    
    Returns:
        delta (float): Solar declination in radians
        subsolar_lon (float): Subsolar point longitude in degrees
    """
    tm = time.gmtime(utc_timestamp)
    N = tm.tm_yday
    hour = tm.tm_hour + tm.tm_min / 60 + tm.tm_sec / 3600

    # Fractional year in radians
    gamma = 2 * math.pi / 365 * (N - 1 + hour / 24)

    # Equation of Time (in minutes)
    EoT = 229.18 * (
        0.000075
        + 0.001868 * math.cos(gamma)
        - 0.032077 * math.sin(gamma)
        - 0.014615 * math.cos(2 * gamma)
        - 0.040849 * math.sin(2 * gamma)
    )

    # Solar declination (in radians)
    delta = (
        0.006918
        - 0.399912 * math.cos(gamma)
        + 0.070257 * math.sin(gamma)
        - 0.006758 * math.cos(2 * gamma)
        + 0.000907 * math.sin(2 * gamma)
        - 0.002697 * math.cos(3 * gamma)
        + 0.00148 * math.sin(3 * gamma)
    )

    # Subsolar longitude (in degrees, range [-180, 180])
    subsolar_lon = (180 - (hour * 15 + EoT * 0.25)) % 360 - 180

    return delta, subsolar_lon

def is_daytime(lon, lat, delta, lambda_s):
    """
    Determine if the (lat, lon) point is in daylight.
    """
    H = math.radians(lon - lambda_s)
    cos_chi = math.sin(-lat) * math.sin(delta) + math.cos(-lat) * math.cos(delta) * math.cos(H)
    return cos_chi <= 0

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