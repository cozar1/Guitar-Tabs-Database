# Guitar Tab database by Cohen Voight

import sqlite3
from colorama import Fore, Style

# Connect to the database
conn = sqlite3.connect('guitar_tabs.db')
cursor = conn.cursor()


# Option to search tabs from id, name or artist
def search_tab(keyword):
    cursor.execute(f"SELECT name, artist, tab, song_genre.genre FROM guitar_tabs JOIN song_genre ON guitar_tabs.genre_id = song_genre.id WHERE name LIKE \"{'%' + keyword + '%'}\";")
    tab = cursor.fetchone()
    print(Fore.YELLOW + '')
    return tab

# displays the tab when succesfully found a search
def display_tab(tab):
    if not tab:
        print(Fore.RED + "No matching tab found.")
    else:
        print(Fore.WHITE + '-' * 60)
        space = ' ' * (20 - len(tab[0]))
        space2 = ' ' * (20 - len(tab[1]))
        print(f'{Fore.CYAN} {tab[0]} {Fore.YELLOW} {space} {tab[1]} {space2} {Fore.RED} {tab[3]}')
        print(Fore.WHITE + '-' * 60)
        print(Fore.YELLOW + tab[2])
        print(Fore.WHITE + '-' * 60)
        
 
 # main code
def main():
    print((Fore.CYAN + '=' + Fore.MAGENTA + '=') * 20)
    print(' ' * 10 + Fore.YELLOW + 'Welcome To Tabmaster')
    print((Fore.MAGENTA + '=' + Fore.CYAN + '=') * 20)
    while True:
        action = input(Fore.BLUE + "\nEnter 'search to search for a tab and 'exit' to exit the program' ").strip().lower()
        #breaks code if exited
        if action == 'exit':
            print(Style.RESET_ALL)
            break

        # searches for a tab option
        elif action == 'search':
            cursor.execute("SELECT name, artist FROM guitar_tabs")
            search_thing = cursor.fetchall()
            print(Fore.CYAN + '')
            for name, artist in search_thing:
                print(Fore.WHITE + '-'*60)
                space = ' ' * (20 - len(name))
                print(f'{Fore.CYAN} {name} {Fore.YELLOW} {space} {artist}')
                print(Fore.WHITE + '-'*60)

            search_term = input(Fore.YELLOW + "Enter a tab name to search: ").strip()
            tab = search_tab(search_term)
            display_tab(tab)

    # Closes the database connection
    conn.close()
 
main()