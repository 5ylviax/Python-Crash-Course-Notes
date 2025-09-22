#Chapter 8 
#Exercise 8-8 User Albums
#Start with your program from exercise 8-7. 
#Write a while loop that allows users to enter an album's artist and title.
#Once you have that information, call make_album() with the user's input and print the dictionary
#that's created. Be sure to include a quit value in the while loop 
def make_album(artist_name, album_title, song_count=None):
    music_album = {'artist_name': artist_name,
                   'album_title': album_title,
                   }
    if song_count:
        music_album['song_count'] = song_count
    
    return music_album


while True:
    print("\nEnter 'q' at any time to quit")
    
    artist_name = input("\tEnter artist name: ")
    if artist_name == 'q':
        break
    album_title = input("\tEnter album title: ")
    if album_title == 'q':
        break
    formatted_album = make_album(artist_name,album_title)
    
    print(f'"{formatted_album['album_title'].title()}" album by {formatted_album['artist_name'].title()}.')
    
    
    