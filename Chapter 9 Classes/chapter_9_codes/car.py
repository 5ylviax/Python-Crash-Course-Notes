class Car: 
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """Add the given amout to the odometer reading"""
        self.odometer_reading += miles
        
my_new_car = Car('audi', 'a4', '2004')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an Attribute's Value Directly 
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute's Value Through a Method 
my_new_car.update_odometer(40)
my_new_car.read_odometer()

# Testing with logic if-else statment 
my_new_car.update_odometer(30)
my_new_car.update_odometer(45)
my_new_car.read_odometer()
print("\n")
#Incrementing an Attribute's Value Through a Method 
my_used_car = Car('subaru', 'outback','2019')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
