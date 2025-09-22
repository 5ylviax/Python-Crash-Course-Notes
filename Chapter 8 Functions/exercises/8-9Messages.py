#Chapter 8 
#Exercise 8-9 Messages: 
#Make a list containing a series of short text messages. Pass the list to a function 
#called show_messages(), which prints each test message 
def show_messages(msg):
    for message in msg:
        print(message)
        
msg = ['copy', 'hello', 'make sure to buy avocados', 'clean the house']

show_messages(msg)