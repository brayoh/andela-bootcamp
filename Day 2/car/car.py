class Car(object):
    num_of_doors = 4
    num_of_wheels = 4
    speed = 0

    def __init__(self, name='General', model='GM', car_type= ''):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.set_properties()

    def set_properties(self):
        two_doors = ['Porshe', 'Koenigsegg']
        if self.name in two_doors:
            self.num_of_doors = 2

        if self.car_type == 'trailer':
            self.num_of_wheels = 8
    
    def is_saloon(self):
        return self.car_type != 'trailer'

    def drive(self, speed):
        if self.car_type == 'trailer':
            self.speed = 77
        else:
            self.speed = pow(10, speed)
        return self
