import unittest
from unittest.mock import MagicMock
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        mock_car_park = MagicMock(spec= CarPark)
        self.entry_sensor = EntrySensor(1, True, mock_car_park)

    def test_entry_sensor_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)



class TestExitSensor(unittest.TestCase):
    def setUp(self):
        mock_car_park = MagicMock(spec= CarPark)
        self.exit_sensor = ExitSensor(1, True, mock_car_park)

    def test_exit_sensor_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)


if __name__ == "__main__":
   unittest.main()
