#Chapter 9-4 Number Served 
# Start with your program from Exercise 9-1 
# Add an attribute called number_served with a default value of 0. ✔ 
# Create an instance called restaurant from this class. ✔

# Print the number of customers the restaurant has served, and then change this value and print it again 
# Add a method called set_number_served() that lets you set the number of customers that have been served ✔
# Call this method with a new number and print the value again ✔
#Add a method called increment_number_served() that lets you increment the number of customers who've been served. 
#Call this method with any number you like that could represent how many customers were served in, say, a day of business

class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name.title()}.")
        print(f"The cuisine type is {self.cuisine_type.title()}.")
        print(f"Total number served {self.number_served}\n")
        
    def open_restaurant(self):
        print(f"The restaurant is open!")
    def set_number_served(self, total):
        self.number_served = total
        print(f"The total number of customers that have been served: {self.number_served}")
        
    def increment_number_served(self, served):  
        self.number_served += served
        
         
        
rest1 = Restaurant('tress caminos', 'mexican')

rest1.describe_restaurant()
rest1.open_restaurant()
rest1.set_number_served(100)
rest1.describe_restaurant()
rest1.increment_number_served(40)
rest1.describe_restaurant()