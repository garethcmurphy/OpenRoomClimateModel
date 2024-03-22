import numpy as np
import matplotlib.pyplot as plt

# Generate random data for the four axes
num_points = 100
thermal_climate = np.random.rand(num_points) * 100
acoustic_climate = np.random.rand(num_points) * 100
atmospheric_climate = np.random.rand(num_points) * 100
visual_climate = np.random.rand(num_points) * 100

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Scatter plot for thermal vs. acoustic climate
axs[0, 0].scatter(thermal_climate, acoustic_climate, color='b', alpha=0.5)
axs[0, 0].set_xlabel('Thermal Climate')
axs[0, 0].set_ylabel('Acoustic Climate')
axs[0, 0].set_title('Thermal vs. Acoustic Climate')

# Scatter plot for visual vs. atmospheric climate
axs[0, 1].scatter(visual_climate, atmospheric_climate, color='r', alpha=0.5)
axs[0, 1].set_xlabel('Visual Climate')
axs[0, 1].set_ylabel('Atmospheric Climate')
axs[0, 1].set_title('Visual vs. Atmospheric Climate')

# Scatter plot for thermal vs. visual climate
axs[1, 0].scatter(thermal_climate, visual_climate, color='g', alpha=0.5)
axs[1, 0].set_xlabel('Thermal Climate')
axs[1, 0].set_ylabel('Visual Climate')
axs[1, 0].set_title('Thermal vs. Visual Climate')

# Scatter plot for atmospheric vs. acoustic climate
axs[1, 1].scatter(atmospheric_climate, acoustic_climate, color='m', alpha=0.5)
axs[1, 1].set_xlabel('Atmospheric Climate')
axs[1, 1].set_ylabel('Acoustic Climate')
axs[1, 1].set_title('Atmospheric vs. Acoustic Climate')

# Adjust layout
plt.tight_layout()

plt.show()
