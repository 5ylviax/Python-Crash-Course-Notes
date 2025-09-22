#Chapter 8 
#Exercise 8-10 Sending Messages 
#Start with a copy of your own program from Exercise 8-9. 
#Write a function called send_messages() that prints each text message and moves each mesage to a new list
#called sent_messages as it's printed. After calling the function, print both of your lists to make sure themessages were moved correctly 


def send_messages(msg):
    while msg:
        message = msg.pop()
        print(message)
        sent_messages.append(message)
        
             
msg = ['copy', 'hello', 'make sure to buy avocados', 'clean the house']
sent_messages = []

send_messages(msg)

print("Final msg list:", msg)  # should be []
print("Sent messages:", sent_messages)  # should contain all messages