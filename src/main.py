from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


c = CarPark("123 Test Street")
print(c)
es = EntrySensor("123", True,c )
exit = ExitSensor("312",True, c)
es.detect_vehicle()
es.detect_vehicle()
exit.detect_vehicle()

print(c.available_bays)