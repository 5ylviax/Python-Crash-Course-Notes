#Chapter 8
#Exercise 8-7 Album 

def make_album(artist_name, album_title, song_count=None):
    music_album = {'artist_name': artist_name,
                   'album_title': album_title,
                   }
    if song_count:
        music_album['song_count'] = song_count
    
    return music_album

info = make_album('lana del rey', 'born to die')
print(info)

info = make_album('harry styles', "harry's house", 13)
print(info)
