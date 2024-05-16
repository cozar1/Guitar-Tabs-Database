# Guitar Tab database by Cohen Voight

import sqlite3
from colorama import Fore

# Connect to the database
conn = sqlite3.connect('guitar_tabs.db')
cursor = conn.cursor()

# option to add tabs
def add_tab(name, artist, tab):
    cursor.execute("INSERT INTO guitar_tabs (name, artist, tab) VALUES (?, ?, ?)", (name, artist, tab))
    conn.commit()
    print(Fore.GREEN + "Tab added successfully!")

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



# removes specific tabs
def remove_tab(name):
    cursor.execute("DELETE FROM guitar_tabs WHERE name = ?", (name,))
    conn.commit()
    print(Fore.GREEN + f"Tab '{name}' removed successfully.")

# deletes all tabs
def delete_tab():
    cursor.execute("DELETE FROM guitar_tabs")
    conn.commit()
    print(Fore.GREEN + "Deleted All tab")

# writes the selected tab to a file


# main code
def main():
    print((Fore.CYAN + '=' + Fore.MAGENTA + '=') * 20)
    print(' ' * 10 + Fore.YELLOW + 'Welcome To Tabmaster')
    print((Fore.MAGENTA + '=' + Fore.CYAN + '=') * 20)
    while True:
        action = input(Fore.BLUE + "\nEnter 'add' to add a tab, 'search' to search for tab, 'remove' to remove a tab, or 'exit' to quit: ").strip().lower()
        #breaks code if exited
        if action == 'exit':
            break
        # deletes all tabs option
        if action == 'delete':
            delete_tab()
        # adds tab option
        if action == 'add':
            name = input(Fore.MAGENTA + "Enter the name of the tab: ")
            artist = input(Fore.MAGENTA + "Enter the artist name: ")
            tab = input(Fore.MAGENTA + "Enter the tab content: ")
            add_tab(name, artist, tab)
        # searches for a tab option
        elif action == 'search':
            search_term = input(Fore.YELLOW + "Enter a tab name or artist name to search: ").strip()
            tab = search_tab(search_term)
            display_tab(tab)

            if tab:
                choice = input(Fore.YELLOW + "Enter the number of the tab to write to file (or '0' to cancel): ")
                try:
                    choice_index = int(choice) - 1
                    if 0 <= choice_index < len(tab):
                        selected_tab = tab[choice_index]
                        name = selected_tab[0]
                        tab_content = selected_tab[2]
                        write_tab_to_file(name, tab_content)
                except ValueError:
                    pass
        # remove tab option
        elif action == 'remove':
            name_to_remove = input(Fore.RED + "Enter the name of the tab you want to remove: ")
            remove_tab(name_to_remove)

    # Closes the database connection
    conn.close()

if __name__ == '__main__':
    main()
