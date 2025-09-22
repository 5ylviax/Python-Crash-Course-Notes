#Chapter 8 Functions 
#----------------------------------------------------FUNCTIONS ----------------------------------------------------
#A function is a block of code which only runs when it is called.
# def means define a function
#----------------------------------------------------Defining a Function ----------------------------------------------------
#def to inform Python that you're defining a function
def greet_user(): #function definition which tells Python the name of the function and, if applicable, what kind of information is need to complete the task.
    #Docstring which describes what the function does 
    #A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. 
    # Such a docstring becomes the __doc__ special attribute of that object.
    
    #For consistency, always use """triple double quotes""" around docstrings. Use r"""raw triple double quotes""" if you use any backslashes in your docstrings.
    """Display a simple greeting."""
    print("Hello!")

#function call tells python to execute the code in the function  
greet_user()

#----------------------------------------------------Passing Information to a Function ----------------------------------------------------
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that are sent to the function when it is called.

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")
    
greet_user('jesse')

greet_user('sarah')

#----------------------------------------------------Arguments and Parameter ----------------------------------------------------
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is a piece of information that's passed from a function call to a function