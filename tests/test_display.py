import unittest
from unittest.mock import MagicMock
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        mock_car_park = MagicMock(spec= CarPark)
        self.display = Display(1, "Welcome to the car park", True, mock_car_park)

    def test_display_with_all_attributes(self):
        self.assertIsInstance(self.display,Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        self.display.update({"message": "Goodbye"})
        print(self.display.message)
        self.assertEqual(self.display.message,"Goodbye")



if __name__ == "__main__":
   unittest.main()


