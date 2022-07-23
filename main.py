from itertools import groupby
from book_class import Book
from simple_term_menu import TerminalMenu
from os import system



# main program
# options = ["Catalogue list", "Search catalogue", "Create entry", "Remove entry", "Modify entry", "Exit"]

def option_menu():
    options = ["Catalogue list", "Search catalogue", "Create entry", "Remove entry", "Modify entry", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    option = options[menu_entry_index]
    return option


# def list_books():
#     pass

# def search_catalogue():
#     pass

def create_entry():
    pass

def remove_entry():
    pass

def modify_entry():
    pass



option = ""

while option != "Exit":
    option = option_menu()
    if option == "Catalogue list":
        print("test")
    elif option == "Search catalogue":
        pass
        # catalogue.display_catalogue()
    elif option == "Create entry":
        create_entry()
    elif option == "Remove entry":
        remove_entry()
    elif option == "Modify entry":
        modify_entry()
    elif option == "Exit":
        continue
    else:
        print("Not a valid option, try again")

print("Success!")

# save to json file here


