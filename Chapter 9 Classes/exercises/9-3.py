# Chapter 9-3 Users: 
# Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile
#Make a method called describe_user() that prints a summary of the user's information.
# Make another method called greet_user() that prints a personalized greeting to the user
# Create several instances representing different users, and call both methods for each user 
class User: 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}\n")
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

user1 = User("silvia","saavedra")
user2 = User("diego", "santiago")
user3 = User("eustorgio", "saavedra")
user4 = User("gustavo", "santiago")
user5 = User("alejandro", "santiago")
user6 = User("ares", "santiago")
user7 = User("ishmael", "santiago")

user1.describe_user()
user2.describe_user()
user3.describe_user()
user4.describe_user()
user5.describe_user()
user6.describe_user()
user7.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
user4.greet_user()
user5.greet_user()
user6.greet_user()
user7.greet_user()
