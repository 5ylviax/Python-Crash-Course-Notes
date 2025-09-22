#Chapter 8 
#section 2 Passing arguments 
#----------------------------------------------------Passing Arguments----------------------------------------------------
#function definiton can have multiple parameters, a function call may need multiple arguments. 
#pass arguments by positional arguments, which need to be in the same order the parameters were written;
#pass arguments by keyword arguments, where each argument consists of a variable name and a value; and lists and dictionaries of values.

#----------------------------------------------------Positional Arguments ----------------------------------------------------
#Arguments are passed in the order of parameters. The order defined in the order function declaration.
#Syntax: FunctionName(value1,value2,value3,....)

#Example --- 
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s names is {pet_name.title()}.")
    
describe_pet('hamster','harry')

#----------------------------------------------------Multiple Function Calls ----------------------------------------------------
# a function can be called as many times as needed.
#Describing a second, different pet requires just one more call to describe_pet()
describe_pet('dog', 'willie')

#----------------------------------------------------Order Matters in Positional Argument ----------------------------------------------------
#Unexpected results if you mix up the order of the arguments in a function call when using positional argument 

describe_pet('harry','hamster')
#----------------------------------------------------Keyword Arguments----------------------------------------------------
#A keyword argument is a name-value pair that you pass to a function.
#Directly associate the name and the value within the argument. 
# Parameter Names are used to pass the argument during the function call.
#Syntax: FunctionName(paramName = value, ....)]


#Keyword-only arguments mean whenever we pass the arguments(or value) by their parameter names at the time of 
# calling the function in Python in which if you change the position of arguments then there will be no change in the output.

#Benefits of using Keyword arguments over positional arguments
#On using keyword arguments you will get the correct output because the order of argument doesn't matter 
# provided the logic of your code is correct. But in the case of positional arguments, you will get more than one output on changing the order of the arguments.

#Both function calls are equivalent
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
#----------------------------------------------------Default Values ----------------------------------------------------
#When writing a function, you can define a default value for each parameter. 
#Default values indicate that the function argument will take that value if no argument value is passed during the function call.
# The default value is assigned by using the assignment(=) operator of the form keywordname=value.

def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
# Using a keyword argument for pet_name,
# so the position does not matter here.

describe_pet(pet_name='willie')

# Here we are using a positional argument for pet_name,
# which is allowed because it matches the first parameter.
# Since we did not specify animal_type, it uses the default 'dog'.

describe_pet('cookie')

#An explicit argument for animal_type is provived. Therefore, Python wil ignore the parameter's default value. 
describe_pet(pet_name='eve', animal_type='cat')

'''When you use default values, any parameter with a default value needs to be listed after all the parameters that don't
have default values. This allows Python to continue interpreting positional arguments correctly. '''

#----------------------------------------------------Equivalent Functon Calls ----------------------------------------------------
#Positional argumetns, keyword arguments, and default values can all be used together, you'll often have several equivalent ways to call function
print("\nEquivalent Functon Calls")
#Example ---
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
#With this defintion an argument always needs to be provided for pet_name and this value can be provided using positional or keyword format

# A dog named Willie 
#Positional
describe_pet('willie')
#keyword 
describe_pet(pet_name='willie')

#A hamster named harry

#Positional
describe_pet('harry','hamster')
#Keyword
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#These function calls produce the same outputs.
#---------------------------------------------------- Avoiding Argument Errors ----------------------------------------------------
#unmatched arguments  occur when you provide fewer or more arguments than a function needs to do its work 

#Example --- 
print("\n---Avoidng Arguments Errors---")
#Python recognizes that some information is missing from the function call and the traceback tells us that
describe_pet()

