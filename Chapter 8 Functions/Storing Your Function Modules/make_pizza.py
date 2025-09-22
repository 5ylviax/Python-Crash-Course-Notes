#importing an entire module 
import pizza


#Importing Specific Functions 

from pizza import make_pizza


pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12, 'muchrooms', 'green peppers', 'extra cheese')

#When python read this file, the line import tells Python to open the file pizza.py and copy all the functions from it into this program

#To call the function form an imported module
#Enter the name of the module
#followed by the name of the function separated by a dot '.'

#Syntax: 
# module_name.function_name()

#Importing files is not limited; therefore, you can import many modules by separating each module name with a comma

#Syntax:
#from module_name import function_0, function_1, function_2 

