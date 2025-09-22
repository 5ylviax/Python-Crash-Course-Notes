#Chapter 8 
#Exercise 8-11 Archived Messages 
#Start with your work form Exercise 8-10. Call the function send_messages() with a copy of the list of messages 
#After calling the function, print both of your list to show that the original list has retained its messages

def send_messages(msg):
    while msg:
        message = msg.pop()
        print(message)
        sent_messages.append(message)
        
             
msg = ['copy', 'hello', 'make sure to buy avocados', 'clean the house']
sent_messages = []

send_messages(msg[:])

print("Final msg list:", msg)  # should be []
print("Sent messages:", sent_messages)  # should contain all messages