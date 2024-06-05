# Guitar Tab database by Cohen Voight
# Guitar tabs are pretty much just more simple music sheets for guitars that give the instructions of how to play the song

import sqlite3

SONG_INFO_SPACING = 30

# Connect to the database
conn = sqlite3.connect('guitar_tabs.db')
cursor = conn.cursor()

# Gets the Guitar tab information to print
def search_tab(keyword):
    cursor.execute(f"SELECT name, artist, tab, song_genre.genre FROM guitar_tabs JOIN song_genre ON guitar_tabs.genre_id = song_genre.id WHERE name LIKE \"{'%' + keyword + '%'}\";")
    tab = cursor.fetchone()
    print('')
    return tab

# displays the tab when succesfully found a search
def display_tab(tab):
    if not tab:
        print("No matching tab found.")
    else:
        print(f'> name: {tab[0]}')
        print(f'> Band: {tab[1]}')
        print(f'> Genre: {tab[3]}')
        print(tab[2])
        print('Scroll up to view tab information:')

# displays the song information with the name, artist and genre
def display_song_information(search_term):
    if not search_term:
        print("\nNo matching tab found.\n")
    else:
        for name, artist, song_genre in search_term:                
            space = '.' * (SONG_INFO_SPACING - len(name))
            space2 = '.' * (SONG_INFO_SPACING - len(artist))
            print(f'\n> {name} {space} {artist} {space2} {song_genre}\n')

# gets the users input for the song/tab that needs to be displayed
def song_input():
    print('Enter a tab/song name to display: ')
    search_term = input("> ").strip()
    if search_term:
        tab = search_tab(search_term)
        display_tab(tab)
        
# main code
def main():

    print('\nWelcome To Tabmaster')

    while True:
        print('''
Please enter an option:
1. Search for a tab by name
2. Search for a tab by Band/Artist
3. Search for a tab by Genre
4. Show all tabs
5. Exit''')
        action = input("> ").strip().lower()
             
        # searches for songs by the name
        if action == '1':
            name = input('Enter Tab Name: ')
            if name:
                cursor.execute(f"SELECT name, artist, song_genre.genre FROM guitar_tabs JOIN song_genre ON guitar_tabs.genre_id = song_genre.id WHERE name LIKE \"{'%' + name + '%'}\";")
                search_term = cursor.fetchall()
                display_song_information(search_term)
                song_input()
        
        # searches for songs by the band/artist
        elif action == '2' or 'band' in action or 'artist' in action:
            artist = input('Enter Artist/Band Name: ')
            if artist:
                cursor.execute(f"SELECT name, artist, song_genre.genre FROM guitar_tabs JOIN song_genre ON guitar_tabs.genre_id = song_genre.id WHERE artist LIKE \"{'%' + artist + '%'}\";")
                search_term = cursor.fetchall()
                display_song_information(search_term)
                song_input()

        # searches for songs by the genre
        elif action == '3' or 'genre' in action:
            genre = input('Enter Genre Name: ')
            if genre:
                cursor.execute(f"SELECT name, artist, song_genre.genre FROM guitar_tabs JOIN song_genre ON guitar_tabs.genre_id = song_genre.id WHERE song_genre.genre LIKE \"{'%' + genre + '%'}\";")
                search_term = cursor.fetchall()
                display_song_information(search_term)
                song_input()
        
        # displays all songs
        elif action == '4' or 'all' in action:
                cursor.execute(f"SELECT name, artist, song_genre.genre FROM guitar_tabs JOIN song_genre ON guitar_tabs.genre_id = song_genre.id")
                search_term = cursor.fetchall()
                display_song_information(search_term)
                song_input()

        # exits the program
        elif action == '5' or 'exit' in action:
            break        

        elif action:
            print('\nyou monkey this isnt an option')

    # Closes the database connection
    conn.close()
 
main()