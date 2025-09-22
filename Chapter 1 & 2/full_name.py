firstName = "silvia"
lastName = "saavedra"
fullName = f"{firstName} {lastName}"
message = f"Hello, {fullName.title()}!"

print(message)
print("Python")
print("\tPython") #Add a tab to you text, use the character combination '\t'

# to add a new line in a string, use the character combination '\n'
print ("Languages: \nPython\nC\nC++\nJavaScript")

#combining tab and new line 
print("Languages: \n\tPython\n\tC\n\tC++\n\tJavaScript\n")

#rstrip() to ensure that no whitespace exists at the right side of a string

userName = "Silvia    "
userLastName = "Saavedra   "
newMessage = f"Hello, {userName.rstrip()} {userLastName.rstrip()}" #necessary when requesting for the user name and last name, if the user adds extra white space.
print(newMessage + "\n")

#strip whitespace from the left side of a string using the 'lstrip()'

favorite_Language = '   python   '
print(favorite_Language.lstrip())  #remove the extra whitespace from the left
print(favorite_Language.rstrip()) #remove the extra whitespace form the right

#to remove white space from both sides 'strip'

print(favorite_Language.strip() + "\n") #in the real world, these stripping function are used most often to clean up user input before it is stored in a program 

#---Removing Prefixes

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://') + "\n")

#Another example

user_Url = 'https://Twitch.tv/5ylvia'

print(user_Url.removeprefix('https://'))

simple_url = user_Url.removeprefix('https://')
print(simple_url)