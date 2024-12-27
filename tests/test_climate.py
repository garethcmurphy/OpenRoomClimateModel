import unittest
import numpy as np
from open_room_climate import ClimateDataGenerator, ClimatePlotter

class TestClimateDataGenerator(unittest.TestCase):
    def test_generate_data(self):
        num_points = 100
        generator = ClimateDataGenerator(num_points)
        data = generator.generate_data()

        self.assertEqual(len(data['thermal_climate']), num_points)
        self.assertEqual(len(data['acoustic_climate']), num_points)
        self.assertEqual(len(data['atmospheric_climate']), num_points)
        self.assertEqual(len(data['visual_climate']), num_points)

        self.assertTrue(np.all(data['thermal_climate'] >= 0) and np.all(data['thermal_climate'] <= 100))
        self.assertTrue(np.all(data['acoustic_climate'] >= 0) and np.all(data['acoustic_climate'] <= 100))
        self.assertTrue(np.all(data['atmospheric_climate'] >= 0) and np.all(data['atmospheric_climate'] <= 100))
        self.assertTrue(np.all(data['visual_climate'] >= 0) and np.all(data['visual_climate'] <= 100))

class TestClimatePlotter(unittest.TestCase):
    def test_plot(self):
        num_points = 100
        generator = ClimateDataGenerator(num_points)
        climate_data = generator.generate_data()

        plotter = ClimatePlotter(climate_data)
        
        # Since plot() method shows the plot which is not testable in a traditional sense,
        # we will just ensure that it runs without errors.
        try:
            plotter.plot()
        except Exception as e:
            self.fail(f"plot() raised {e.__class__.__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()