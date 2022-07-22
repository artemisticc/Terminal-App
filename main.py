# from itertools import groupby
# from book_item import BookItem
from simple_term_menu import TerminalMenu



# main program
def main():
    options = ["Display Catalogue", "Search catalogue", "Create entry", "Delete entry", "Modify entry"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"Searching for books using '{options[menu_entry_index]}'.")

if __name__ == "__main__":
    main()

