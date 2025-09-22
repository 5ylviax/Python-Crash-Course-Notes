#Chapter 4 Exercise 4-5 Summing a Million
'''
Make a list of the numbers form one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million.
Also, use the sum() function to see how quikcly Python can add a million numbers
'''
numbers = list(range(1,1_000_001))
print(f"The minimum number is ", min(numbers))
print("The maximum number is ", max(numbers))
print("The sum of the list is ", sum(numbers))

