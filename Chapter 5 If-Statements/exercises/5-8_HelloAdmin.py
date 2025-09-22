#Chapter 5 
#Exercise 5-8 Hello Admin
#Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each suer afeter they log
# in to a website. Loop through the list, and print a greeting to each user 
usernames = ['silviaxp','XxPaper','jaden__','paperclipxX', 'admin','finalmouseXp']

#If the username 'admin', print a special greeting, such as "Hello admin, would you like to see a status report?"
for username in usernames:
    if username == 'admin':
        print("Hello Admin, would you like to see a status report?")
#Otherwise, print a generic greeting, such as "Hello Jaden, thank you for logging in again"
    else:
        print(f"Hello {username.title()}, thank you for logging in again!")

