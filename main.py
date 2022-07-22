from itertools import groupby
from book_item import BookItem
from simple_term_menu import TerminalMenu

from program.catalogue import Catalogue



# main program
def option_menu():
    options = ["List books (by title)", "Search catalogue", "Create entry", "Remove entry", "Modify entry", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    # print(f"Searching for books using '{options[menu_entry_index]}'.")

def list_books():
    pass

def search_catalogue():
    pass

def create_entry():
    pass

def remove_entry():
    pass

def modify_entry():
    pass



options = ""

while options != "Exit":
    option = option_menu()
    if option == "List books (by title)":
        pass
    elif option == "Search catalogue":
        pass
    elif option == "Create entry":
        pass
    elif option == "Remove entry":
        pass
    elif option == "Modify":
        pass
    elif option == "Exit":
        continue
    else:
        print("Not a valid option, try again")

# save to json file here