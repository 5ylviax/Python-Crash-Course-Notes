#Chapter 8 
#Exercise 8-4 Large Shirts 
#Modify the make_shirts() function so that shirts are large by default with a message that reads "I love Python"
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message. 

def make_shirt(size='large', message='I love Python!'):
    print(f"The size of the shirt is {size} and the text that should be printed on the shirt must say: ")
    print(f"\t{message}")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt('medium')

# Small shirt with a different message
make_shirt('small', 'Keep Calm and Code On')