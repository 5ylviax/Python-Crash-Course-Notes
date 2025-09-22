#3-1 Names: Printing individuals friends names
friends = ['Unknown', 'Maria','Krista', 'Jr.', 'Sophia','silvia']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
#3-2 Greetings

message = f"Hello, how are you doing {friends[0]}?"
print(message)
print(f"Hello, how are you doing {friends[1]}?")
print(f"Hello, how are you doing {friends[2]}?")
print(f"Hello, how are you doing {friends[3]}?")
print(f"Hello, how are you doing {friends[4]}?")

print("\3-3 Your own list:\n")
#3-3 Your Own List
carsOwned = ['testla', 'ford','nissan','toyota','kia','gmc','ram','porsche']
message = f'{friends[-1].title()} said "I would like to own a {carsOwned[-1].title()}"'
print(message)