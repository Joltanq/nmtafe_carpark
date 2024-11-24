from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self,location = "Unknown", capacity = 100, plates = None, sensors = None, displays = None):
        self.location = location
        self.capactiy = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f'Car park at {self.location} with {self.capactiy} bays'

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.sensors.append(component)


    def add_car(self):
        ...

    def remove_car(self):
        ...

    def update_displays(self):
        ...



c = CarPark()
c.register(Sensor(1, True, "513"))
c.register(Display())
print(c)