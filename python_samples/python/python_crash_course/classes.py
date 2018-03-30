""" A SIMPLE REPRESENTATION OF CLASSES IN PYTHON """
class Car():

    def __init__(self,year,make,model):
        self.year=year
        self.make=make
        self.model=model
        self.odometer_reading=70

    def change_odometer_reading(self,value):
        if value > self.odometer_reading:
            self.odometer_reading=value
        else:
            print('Cannot Override odometer reading')
        
    def get_odometer_reading(self):
        print('The odometer reading is '+str(self.odometer_reading))


class ElectricCar(Car):

    def __init__(self,year,make,model):
        super().__init__(year,make,model)
        self.battery=Battery()

class Battery():

    def __init__(self,battery=10):
        self.battery=battery

    def show_battery_capacity(self):
        print('The battery capacity is '+str(battery)+'-kwh')

    
my_tesla = ElectricCar(2017,'Tesla ','Model-S ')
my_tesla.show_battery_capacity()
    
