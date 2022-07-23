from itertools import groupby
from book_class import Book
from catalogue import Catalogue
from simple_term_menu import TerminalMenu
from os import system
import shelve


# main program
# options = ["Catalogue list", "Search catalogue", "Create entry", "Remove entry", "Modify entry", "Exit"]

def main_menu():
    options = ["Catalogue list", "Search catalogue", "Create entry", "Remove entry", "Modify entry", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    option = options[menu_entry_index]
    return option

def modify_menu():
    modify_options = ["Title", "Author", "Price", "Stock Count", "Exit"]
    terminal_menu = TerminalMenu(modify_options)
    menu_entry_index = terminal_menu.show()
    option = modify_options[menu_entry_index]
    return option

# def list_books():
#     pass

# def search_catalogue():
#     pass

def create_entry():
    pass
    Book.create_book()


def remove_entry():
    pass



def modify_entry():
    modify = ""
    while modify != "Exit":
        modify = modify_menu()
        if modify == "Title":
            print("test")
        elif modify == "Author":
            pass
        elif modify == "Price":
            pass
        elif modify == "Stock Count":
            pass
        elif modify == "Exit":
            continue
        else:
            print("Not a valid option, try again")






while option != "Exit":
    option = ""
    option = main_menu()
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
        print("I don't know how you managed to pick something that doesn't exist, but it's not valid, so try again")

print("Success!")
my_data_file.close()
# save to json file here


