#Chapter 8 Section 6 
#----------------------------------------------------Storing Your Function in Modules ----------------------------------------------------
#The advantage of functions is to separate the block of code from the main program. 

#Adding another tool for readability is done by storing the function in a separate file called a module.
#Importing the module into the main program is called import. Import statement tells the python to make the code in a module available 
# in the currently running program file.  

#----------------------------------------------------Importing an Entire Model ----------------------------------------------------
#A module is a file that ends with title_of_file.py and contains a block of code you want to import into your main program.
#Create another separate file called making_pizza.py, which will be the main program, in the same directory as pizza.py.
#This file will import the functions from the module and make two calls for clean readability of the code.


#When python read this file, the line import tells Python to open the file pizza.py and copy all the functions from it into this program

#To call the function form an imported module
#Enter the name of the module
#followed by the name of the function separated by a dot '.'

#Syntax: 
# module_name.function_name()

#----------------------------------------------------Importing Specific Functions ----------------------------------------------------

#Importing functions is not limited; therefore, you can import many functions by separating each function name with a comma.

#Syntax:
#from module_name import function_0, function_1, function_2 

#With this syntax, you dont have to call the fucntion by using the dot notation, therefore we can call the function by its name 


# ---------------------------------------------------- Using `as` to Give a Function an Alias ----------------------------------------------------
# If the name of a function conflicts with an existing name in the main program, or if the function name is too long,
# this can be resolved by using a unique alias—an alternate name similar to a nickname for the function.

#Renames the function make_pizza to mp by the keyword 'as'
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'muchrooms', 'green peppers', 'extra cheese')

#Syntax: 
# form module_name import function as fn 


# ---------------------------------------------------- Using 'as' to Give a Module an Alias ----------------------------------------------------
# an alias can also be given to a module name. 

import pizza as p 

#The module is given an alias "p" in the  import statement. All the function within the module retains their original names. 

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'muchrooms', 'green peppers', 'extra cheese')

#Syntax: 
# import module_name as mn

# ---------------------------------------------------- Importing All Functions in a Module ----------------------------------------------------
#To import all the functions in a module by using the saterick (*) operator 

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'muchrooms', 'green peppers', 'extra cheese')
#Syntax: 
# from module_name import * 


#The asterick in the import statement tells Python to copy every function from the module into the main program 
# Since every function is imported, each function can be called by their name's without using the dot notation 

'''
Avoid this when workin with large modules 
Best approach is to import function or functions you want, or import the entire module and use the dot notation
'''

# ---------------------------------------------------- Styling Functions ----------------------------------------------------
#Functions should have descriptive names, and these names should lowercase laetters and underscores. 
#Module names should use these convention as well 


#Every functions should have a commment that explains concisely what the function does 
#comment should appear immeadiately after the function definition and use the doc string format 

#PEP 8 
#example 

# def function_name(
    #parameter_0, parameter_1, parameter_2,
    #parameter_3, parameter_4, parameter_5,
    #)
    #
    #
    #Function body... 
    

#all import statements should be written at the beginning of a file. 


