#Chapter 8 
#Exercise 8-2 Favorite Book 
#Write a function called favorite_book()  that accepts one parameter, title. The function should print a message, such as
#"One of my favorite book is Alice in Wonderland." Call the function, making sure to include a book title as an argument in the function call 

def favorite_book(book_name):
    print(f"One of my favorite book is {book_name.title()}.")

favorite_book('Alice in wonderland')