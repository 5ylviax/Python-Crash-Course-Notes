#Chapter 6
#Exercise 6-2: Glossary 2:
glossary = {'dictionary': 'a dictionary in Python is a collection of key-value pairs.',
            'list': 'a data structure in Python that is a mutable, or changeable, ordered sequence of elements.',
            'runtime': 'when the code is actually executing. Things can change dynamically.',
            'traverse': 'to sysematically visit or access each element within a data strcuture, such as an array, linked list, or tree, typically to perform some operation on each element.',
            'for loop': 'is used to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects.',
            }
# Now that you know how to loop through a dictionary, clean up the code from exercise 6-3 by replacing your series of print()
#calls with a loop that runs through the dictionary's keys and values.

for word, definiton in glossary.items():
    print(f"{word.title()}: {definiton}")
    
# When you're sure that your loop works, add five more Python terms to your glossary. 
glossary['set'] = 'is a collection of unique, unordered, and mutable elements.'
glossary['nesting'] = 'a list of items as a vlaue in a dictionary'
glossary['key'] = 'is a unique indentifier used to access a specific value within a dictionary.'
glossary['value'] = ' is the data associated with a specific key.'
glossary['item'] = 'an "itme" refers to key-value pair considered as a single unit. Its a combination of a key and its associated value.'

#When you run your program again, these new words and meaning should automatically be included in the output 

print("\nAfter adding the new words to the glossary. \n")
for word, definiton in glossary.items():
    print(f"{word.title()}: {definiton}")
