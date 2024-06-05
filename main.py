# Guitar Tab database by Cohen Voight

import sqlite3

# Connect to the database
conn = sqlite3.connect('guitar_tabs.db')
cursor = conn.cursor()


# Option to search tabs from id, name or artist
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
        print('#' * 60)
        print(f'> name: {tab[0]}')
        print(f'> Band: {tab[1]}')
        print(f'> Genre: {tab[3]}')
        print('-' * 60)
        print(tab[2])
        print('#' * 60)
        
 
 # main code
def main():
    print(('=') * 40)
    print(' ' * 10 +'Welcome To Tabmaster')
    print(('=') * 40)
    while True:
        print('Please enter an option:')
        print('1. Search for a tab by name')
        print('2. Search for a tab by  Band/Artist')
        print('3. Search for a tab by Genre')
        print('4. Show all tabs')
        print('5. Exit')
        action = input("> ").strip().lower()
        #breaks code if exited
        if action == '5':
            break
        
        elif action == '2':
            artist = input('Enter Artist/Band Name: ')
            cursor.execute(f"SELECT name, artist FROM guitar_tabs WHERE artist LIKE \"{'%' + artist + '%'}\";")
            search_thing = cursor.fetchall() 
            print('')           
            for name, artist in search_thing:                
                space = '.' * (30 - len(name))
                print(f'> {name} {space} {artist}')
            print('')           
                
            print('Enter a tab name to display: ')
            search_term = input("> ").strip()
            tab = search_tab(search_term)
            display_tab(tab)


        # searches for a tab option
        elif action == '1':
            name = input('Enter Tab Name: ')
            cursor.execute(f"SELECT name, artist FROM guitar_tabs WHERE name LIKE \"{'%' + name + '%'}\";")
            search_thing = cursor.fetchall()
            print('')  
            for name, artist in search_thing:
                space = '.' * (30 - len(name))
                print(f'> {name} {space} {artist}\n')
            print('')           


            print('Enter a tab name to display: ')
            search_term = input("> ").strip()
            tab = search_tab(search_term)
            display_tab(tab)

    # Closes the database connection
    conn.close()
 
main()