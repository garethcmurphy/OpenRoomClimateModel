import numpy as np
import matplotlib.pyplot as plt

class ClimateDataGenerator:
    def __init__(self, num_points):
        self.num_points = num_points

    def generate_data(self):
        return {
            'thermal_climate': np.random.rand(self.num_points) * 100,
            'acoustic_climate': np.random.rand(self.num_points) * 100,
            'atmospheric_climate': np.random.rand(self.num_points) * 100,
            'visual_climate': np.random.rand(self.num_points) * 100
        }

class ClimatePlotter:
    def __init__(self, climate_data):
        self.climate_data = climate_data

    def plot(self):
        fig, axs = plt.subplots(2, 2, figsize=(10, 8))

        self._scatter_plot(axs[0, 0], 'thermal_climate', 'acoustic_climate', 'b', 'Thermal vs. Acoustic Climate')
        self._scatter_plot(axs[0, 1], 'visual_climate', 'atmospheric_climate', 'r', 'Visual vs. Atmospheric Climate')
        self._scatter_plot(axs[1, 0], 'thermal_climate', 'visual_climate', 'g', 'Thermal vs. Visual Climate')
        self._scatter_plot(axs[1, 1], 'atmospheric_climate', 'acoustic_climate', 'm', 'Atmospheric vs. Acoustic Climate')

        plt.tight_layout()
        plt.show()

    def _scatter_plot(self, ax, x_key, y_key, color, title):
        ax.scatter(self.climate_data[x_key], self.climate_data[y_key], color=color, alpha=0.5)
        ax.set_xlabel(x_key.replace('_', ' ').title())
        ax.set_ylabel(y_key.replace('_', ' ').title())
        ax.set_title(title)

if __name__ == "__main__":
    num_points = 100
    generator = ClimateDataGenerator(num_points)
    climate_data = generator.generate_data()

    plotter = ClimatePlotter(climate_data)
    plotter.plot()
