#Chapter 6
#Exercise 6-3: A python dictionary can be used to model an actual dictionary. 
#However, to avoid confusion, let's call its a glossary. 

#Think of five programming words you've learned about in the previous chpaters. Use these words as the keys in your glossary, 
# and store their meanings as values. 
glossary = {'dictionary': ': a dictionary in Python is a collection of key-value pairs.',
            'list': ': a data structure in Python that is a mutable, or changeable, ordered sequence of elements.',
            'runtime': ': when the code is actually executing. Things can change dynamically.',
            'traverse': 'to sysematically visit or access each element within a data strcuture, such as an array, linked list, or tree, typically to perform some operation on each element.',
            'for loop': ': is used to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects.',
            }

#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then
#print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word- meaning pair in your output.

print(f"Dictionary{glossary['dictionary']}")
print(f"List{glossary['list']}")
print(f"Runtime{glossary['runtime']}")
print(f"Traverse{glossary['traverse']}")
print(f"For loop{glossary['for loop']}")
