invite = []
invite.append('Ares')
invite.append('Alejandro')
invite.append('Diego')
invite.append('Eustorgio')
invite.append('Ishmael')
invite.append('Gustavo')

unable = invite.pop() # returns a value 

print(f'He is unable to attend to the dinner {unable}, he dislikes Hamburgers')

invite.append('Mom') # inserts a value into the list 


message = f'You guys are invited to the cook out: \n\t{invite[0]}\n\t{invite[1]}\n\t{invite[2]}\n\t{invite[3]}\n\t{invite[4]}\n\t{invite[5]}'
print(message)


#3-6 More Guests
print(f'A bigger table has been found')
invite.insert(-1,'Dad')
invite.insert(0,'Aunt')
invite.insert(4,'Uncle')
print(invite)

#3-7 Shrinking Guest List: 
print('Only two people can be invited')
name = invite.pop()
print(f'Sorry, you cannot attend to dinner {name.title()}')
name= invite.pop()
print(f'Sorry, you cannot attend to dinner {name.title()}')
name= invite.pop()
print(f'Sorry, you cannot attend to dinner {name.title()}')
name= invite.pop()
print(f'Sorry, you cannot attend to dinner {name.title()}')
name= invite.pop()
print(f'Sorry, you cannot attend to dinner {name.title()}')
name= invite.pop()
print(f'Sorry, you cannot attend to dinner {name.title()}')
name= invite.pop()
print(f'Sorry, you cannot attend to dinner {name.title()}')

print(invite)

print(f'letting you know that you are still invited {invite[0]}')
print(f'You are stil invited {invite[-1]}')

del invite[0]
del invite[0]
print(invite)