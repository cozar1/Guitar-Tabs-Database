# Guitar Tab database by Cohen Voight

import sqlite3
from colorama import Fore

# Connect to the database
conn = sqlite3.connect('guitar_tabs.db')
cursor = conn.cursor()

# Option to search tabs from id, name or artist
def search_tab(keyword):
    cursor.execute("SELECT name, artist, tab FROM guitar_tabs WHERE name LIKE ? OR artist LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
    tab = cursor.fetchone()
    print(Fore.YELLOW + '')
    return tab

# displays the tab when succesfully found a search
def display_tab(tab):
    if not tab:
        print(Fore.RED + "No matching tab found.")
    else:
        print(Fore.BLUE + '-' * 60)
        print(Fore.MAGENTA + tab[0])
        print(Fore.CYAN + tab[1])
        print(Fore.YELLOW + tab[2])
        print(Fore.BLUE + '-' * 60)
 
# main code
def main():
    print((Fore.CYAN + '=' + Fore.MAGENTA + '=') * 20)
    print(' ' * 10 + Fore.YELLOW + 'Welcome To Tabmaster')
    print((Fore.MAGENTA + '=' + Fore.CYAN + '=') * 20)
    while True:
        action = input(Fore.BLUE + "\nEnter 'search to search for a tab and 'exit' to exit the program'").strip().lower()
        #breaks code if exited
        if action == 'exit':
            break

        # searches for a tab option
        elif action == 'search':
            search_term = input(Fore.YELLOW + "Enter a tab name or artist name to search: ").strip()
            tab = search_tab(search_term)
            display_tab(tab)

    # Closes the database connection
    conn.close()

if __name__ == '__main__':
    main()
