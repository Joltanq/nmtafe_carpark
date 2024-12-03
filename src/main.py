from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


# DONE TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
# DONE - TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
# DONE TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
# DONE TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
# DONE TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
# DONE TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)

car_park = CarPark.from_config("config.json")
entry_sensor = EntrySensor(1, True,car_park )
exit_sensor = ExitSensor(2,True, car_park)
display = Display(1, "Welcome to Moondalup", True, car_park)
car_park.register(display)
car_park.register(entry_sensor)
car_park.register(exit_sensor)

for _ in range(10):
    entry_sensor.detect_vehicle()

for _ in range(2):
    exit_sensor.detect_vehicle()

print(display)

