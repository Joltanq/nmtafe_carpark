class Sensor:
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f'{self.id} status is {self.is_active} at {self.car_park}'

class EntrySensor(Sensor):
    ...

class ExitSensor(Sensor):
    ...


entry = EntrySensor(1, True, "123 Test Street" )
print(entry)