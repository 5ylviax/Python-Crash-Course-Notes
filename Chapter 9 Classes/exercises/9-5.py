#Chapter 9-5 Login Attempt 
# ADD an attribute called login_attempts to your User class form Exercise 9-3 (page 162). 
# Write a method called increment_login_attempts() that increment the value of login_attempts by 1
# Write another method called reset_login_attempts() that resets the value of login_attempt to 0
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly, adn then call reset_login_attempts(). 
# Print login_attempts again to make sure it was reset to 0

class User: 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}\n")
    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    
user1 = User('silvia', 'saavedra')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"{user1.login_attempts}")

user1.reset_login_attempts()
print(f"{user1.login_attempts}")
    