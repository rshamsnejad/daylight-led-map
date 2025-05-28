import numpy as np
import time
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def sun_position(utc_timestamp):
    tm = time.gmtime(utc_timestamp)
    N = tm.tm_yday
    hour = tm.tm_hour + tm.tm_min / 60 + tm.tm_sec / 3600
    gamma = 2 * np.pi / 365 * (N - 1 + hour / 24)
    EoT = 229.18 * (0.000075 + 0.001868*np.cos(gamma) - 0.032077*np.sin(gamma)
                    - 0.014615*np.cos(2*gamma) - 0.040849*np.sin(2*gamma))
    delta = (0.006918 - 0.399912*np.cos(gamma) + 0.070257*np.sin(gamma)
             - 0.006758*np.cos(2*gamma) + 0.000907*np.sin(2*gamma)
             - 0.002697*np.cos(3*gamma) + 0.00148*np.sin(3*gamma))
    subsolar_lon = (180 - (hour * 15 + EoT * 0.25)) % 360 - 180
    return delta, subsolar_lon

def is_daytime(lat, lon, delta, lambda_s):
    """
    Determine if the (lat, lon) point is in daylight.
    """
    H = np.radians(lon - lambda_s)
    cos_chi = np.sin(-lat) * np.sin(delta) + np.cos(-lat) * np.cos(delta) * np.cos(H)
    return cos_chi <= 0

# Get current UTC timestamp
time_to_plot = time.time()
# time_to_plot = time.mktime(time.strptime("Tue, 03 Aug 2021 10:45:08", "%a, %d %b %Y %H:%M:%S"))
# time_to_plot = time.mktime(time.strptime("20 March 2025 09:00:00", "%d %B %Y %H:%M:%S"))

# Calculate sun position
delta, lambda_s = sun_position(time_to_plot)


density_factor = 4

# Create latitude and longitude grid (1° spacing)
lat_grid = np.radians(np.linspace(-90, 90, 16 * density_factor))
lon_grid = np.linspace(-180, 180, 32 * density_factor)
Lon, Lat = np.meshgrid(lon_grid, lat_grid)

# Classify points as day or night
day_night_mask = np.vectorize(lambda lat, lon: is_daytime(lat, lon, delta, lambda_s))(Lat, Lon)

# Convert radians to degrees for plotting
Lat_deg = np.degrees(Lat)

# Plot
plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

# Plot daytime points (yellow) and nighttime points (blue)
ax.scatter(Lon[day_night_mask], Lat_deg[day_night_mask], color='gold', s=1, label='Day')
ax.scatter(Lon[~day_night_mask], Lat_deg[~day_night_mask], color='midnightblue', s=1, label='Night')

plt.title(f'Day and Night Grid (based on Terminator) at {time_to_plot} UTC')
plt.legend(loc='lower left')
plt.show()