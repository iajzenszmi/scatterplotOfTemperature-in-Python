import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Simulate hourly temperature data (24 hours)
hours = np.arange(24)

# Simulate yesterday's temperatures (baseline sine curve + noise)
yesterday_base = 15 + 10 * np.sin((hours - 6) * np.pi / 12)  # warmest at 2pm
yesterday_temps = yesterday_base + np.random.normal(0, 1.0, size=24)

# Simulate today's temperatures with slight variation from yesterday
today_temps = yesterday_temps + np.random.normal(0, 1.5, size=24)

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(yesterday_temps, today_temps, color='blue', alpha=0.7, edgecolor='k')
plt.plot([min(yesterday_temps), max(yesterday_temps)],
         [min(yesterday_temps), max(yesterday_temps)],
         color='red', linestyle='--', label='y = x (equal temp)')
plt.xlabel("Yesterday's Temperature (°C)")
plt.ylabel("Today's Temperature (°C)")
plt.title("Scatterplot: Today's vs Yesterday's Temperatures")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
