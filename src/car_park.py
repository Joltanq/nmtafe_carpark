from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self,location = "Unknown", capacity = 3, plates = None, sensors = None, displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f'Car park at {self.location} with {self.capacity} bays now has {self.available_bays} free bays'

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.sensors.append(component)


    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25, "message": "Welcome"}
        for display in self.displays:
            display.update(data)
        return data

        # for display in self.displays:
        #     print(f"updating display {display.id}")
        #     display.update(f"Bays:" {self.capacity} - len({self.plates}) )

    @property
    def available_bays(self):
        if self.capacity - len(self.plates) < 0:
            return 0
        else:
            return self.capacity - len(self.plates)

