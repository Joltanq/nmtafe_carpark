from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entries
import json

class CarPark:
    def __init__(self,location = "Unknown", capacity = 100, plates = None, sensors = None, displays = None, log_file = "test.txt"):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file,Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return f'Car park at {self.location} with {self.capacity} bays now has {self.available_bays} free bays'

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)


    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays({"The number of available bays is ": self.available_bays, "The current temperature is ": 25})
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays({"The number of available bays is ": self.available_bays, "The current temperature is ": 25})
        self._log_car_activity(plate, "exited")

    def update_displays(self,data={}):
        self.data = data
        # data = {"The number of available bays is ": self.available_bays, "The current temperature is": 25}
        for display in self.displays:
            display.update(data)
        return data

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
        with open("config.json","w") as f:
            json.dump({"location":self.location, "capacity": self.capacity, "log_file": str(self.log_file)},f)


    @classmethod
    def from_config(cls,config_file = Path("config.json")):
        config_file = config_file if isinstance(config_file,Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(location = config["location"],
                   capacity= config["capacity"],
                   plates = config["plates"],
                   sensors = config["sensors"],
                   displays = config["displays"],
                   log_file = config["log_file"])

    @property
    def available_bays(self):
        if self.capacity - len(self.plates) < 0:
            return 0
        else:
            return self.capacity - len(self.plates)

