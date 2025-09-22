# ---------------------------------------------------------------Integers -------------------------------------------------------
print(2 + 3)
print(3-2)
print(2 * 3)
print(3/2)
print(2**0) #python uses two multiplicaton symbols to represent exponents 
print(2**3)
#Python supports order of operation 
# - can use multiple operations in one expression 
# - parentheses to modify the order of operation
print(2 + 3 * 4)
print((2+ 3) * 4)
#the spacing in these examples has no effect on how Python evaluates the expressions 

# -------------------------------------------------------------------Floats -----------------------------------------------------
# Python calls any numbers with a decimal points a 'float', it is used in most programming languages, and it is refers to the fact that a decimal point
#can appear at any position in a number
print(0.1 + 0.1 )
print(0.2 + 0.2)
print(2* 0.1)
#However, be aware that you can sometimes get an arbitrary number of decimal places in your answer

print(0.2 + 0.1 )
print(3 * 0.1 )

#When you divide any two numbers, even if they are integers that result in a whole number, you'll always get a float 
print("Dividing any two numbers", 4/2) #output : 2.0
#even when mixing integers and a float in any other operation 

print(1 + 2.0 )
print(2 * 3.0)
print(2.0 ** 6)

#------------------------------------------------------------Underscores in Numbers --------------------------------------------------------------------------------
#When writing long numbers, you can group using underscores to make large numbers more readable

universe_age=(14_000_000_000)
print(universe_age)
#Python ignores the underscores,even if you do not group the digits in threes, the values will still be unaffected.
#------------------------------------------------------------Multiple Assignment --------------------------------------------------------------------------------
x, y, z = 0,0,0
print(x + y + z )
x, y, z = 1, 2 ,3 
print(x + y + z )

#------------------------------------------------------------Constants --------------------------------------------------------------------------------
#constant -- is a variable whose values stays the same throughout the life of a program
#Python does not have built-in constant types but Python programmers use all capital letters to indicate a variable should be treated as a constant 
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)