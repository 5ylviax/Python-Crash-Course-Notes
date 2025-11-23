#Chapter 9
# Exercise 9-1 Restuarant
# Make a class called Restuarant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method call describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open 
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods 

class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"The restaurant is open!")
    
rest1 = Restaurant("Tres Caminos", "mexican")
# Make an instance 
print(f"The restaurant name is: {rest1.restaurant_name.title()}")
print(f"The resturant cuisiine type is: {rest1.cuisine_type.title()}\n")

# Printing the two attributes individuall using call methods 
rest1.describe_restaurant()
rest1.open_restaurant()



    