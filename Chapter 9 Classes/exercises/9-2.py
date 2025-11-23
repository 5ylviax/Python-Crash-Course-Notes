# Exercise 9-2 Three Restaurant
# Start with your class from Exercise 9-1.
# Create three different instances from the class, and call describe_restaurant() for each instance 
class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name.title()}.")
        print(f"The cuisine type is {self.cuisine_type}.\n")
        
    def open_restaurant(self):
        print(f"The restaurant is open!")
        
rest1 = Restaurant("tres caminos", "mexican")
rest2 = Restaurant("gingers", "chinese cuisine")
rest3 = Restaurant("hokkaido", "japanese")

rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()

 