import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.entry_sensor = EntrySensor(1, True, CarPark(...))

    def test_entry_sensor_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)



class TestExitSensor(unittest.TestCase):
    def setUp(self):
        self.exit_sensor = ExitSensor(1, True, CarPark(...))

    def test_exit_sensor_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)


if __name__ == "__main__":
   unittest.main()
