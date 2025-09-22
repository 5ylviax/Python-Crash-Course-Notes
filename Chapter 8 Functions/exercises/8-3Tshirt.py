#Chater 8 
#Exercise 8-3 T-Shirt 
#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print
#a sentence summarzing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. 
#Call the function a second times using keyword arguments 

def make_shirt(size, text_message):
    print(f"The size of the shirt is {size} and the text that should be printed on the shirt must say: ")
    print(f"\t{text_message}")

#Positional arguments
make_shirt('medium','A function does not always have to display its output directly')
#Keyword arguments 
make_shirt(size='large',text_message='Avoiding Argument Errors')
    