from abc import ABC, abstractmethod
import random
class Sensor(ABC):
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f'{self.id} status is {self.is_active} at {self.car_park}'

    @abstractmethod
    def update_car_park(self,plate):
        pass

    # 03d specifies the format of the int that should be returned.
    # in this case 3 digits and pad it with 0 if its a singular digit
    def _scan_plate(self):
        return "FAKE-" + format(random.randint(0,999), "03d")


    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    def update_car_park(self,plate):
        print(f"Incoming vehicle detected. Plate: {plate}")
        self.car_park.add_car(plate)

class ExitSensor(Sensor):
    def update_car_park(self,plate):
        print(f"Outgoing vehicle detected. Plate: {plate}")
        self.car_park.remove_car(plate)

    def _scan_plate(self):
        return random.choice(self.car_park.plates)



