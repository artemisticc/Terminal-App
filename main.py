from book_class import Book
from simple_term_menu import TerminalMenu
from termcolor import colored, cprint
from tabulate import tabulate
from art import *
import pandas as pd
from colorama import init


catalogue_objects = []

# menus
def main_menu():
    cprint("What would you like to do?", "blue", attrs=["bold"])
    options = ["Catalogue list", "Search catalogue", "Create entry", "Remove entry", "Modify entry", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    option = options[menu_entry_index]
    return option

def search_menu():
    cprint("What would you like to search by?", "blue", attrs=["bold"])
    modify_options = ["Title", "Author", "Exit"]
    terminal_menu = TerminalMenu(modify_options)
    menu_entry_index = terminal_menu.show()
    option = modify_options[menu_entry_index]
    return option

def modify_menu():
    cprint("What would you like to modify about this entry?", "blue", attrs=["bold"])
    modify_options = ["Title", "Author", "Price", "Stock Count", "Exit"]
    terminal_menu = TerminalMenu(modify_options)
    menu_entry_index = terminal_menu.show()
    option = modify_options[menu_entry_index]
    return option

# program functions
def _update(key1, key2, item_index, type=str,):
        try:
            a = colored("Updated " + key1 + ": ", "grey", attrs=["bold"])
            x = type(input(a))
            if not x:
                _failed(key1)
                return
            y = {key2: x}
            catalogue_objects[item_index].update(y)
            cprint("Entry updated successfully.", "green", attrs=["bold"])
        except ValueError:
            _failed(key1)
            return

def _return():
    cprint("Returning to main menu.", "magenta", attrs=["bold"])

def _failed(key1):
    cprint("Failed to update " + key1 + ".", "red", attrs=["bold"])

def _print_df(var):
    df = pd.DataFrame(var)
    print(tabulate(df, headers=["Title","Author", "Price($)", "Stock"], tablefmt="fancy_grid"))

def _search_title():
    question = colored("What title are you looking for? ", "blue", attrs=["bold"])
    title_var = input(question)
    n = 0
    x = list(filter(lambda item: item["title"] == title_var, catalogue_objects))
    for item in catalogue_objects:
        if item["title"] == title_var:
            n += 1
    if n == 1:
        cprint("There is " + str(n) + " book with this title in the system.", "green", attrs=["bold"])
        _print_df(x)
        return n
    elif n > 1:
        cprint("There are " + str(n) + " books with this title in the system.", "green", attrs=["bold"])
        _print_df(x)
        return n
    else:
        cprint("There are no books with this title in the system.", "magenta", attrs=["bold"])
        return n

def _search_author():
    question = colored("What author are you looking for? ", "blue", attrs=["bold"])
    author_var = input(question)
    n = 0
    x = list(filter(lambda item: item["author"] == author_var, catalogue_objects))
    for item in catalogue_objects:
        if item["author"] == author_var:
            n += 1
    if n == 1:
        cprint("There is " + str(n) + " book with this author in the system.", "green", attrs=["bold"])
        _print_df(x)
    elif n > 1:
        cprint("There are " + str(n) + " books with this title in the system.", "green", attrs=["bold"])
        _print_df(x)
    else:
        cprint("There are no books with this author in the system.", "magenta", attrs=["bold"]) 


# main feature functions
def catalogue_list():
    tprint("catalogue")
    _print_df(catalogue_objects)

def search_catalogue():
    search = ""
    try:
        while search != "Exit":
            search = search_menu()
            print(search)
            if search == "Title":
                _search_title()
            elif search == "Author":
                _search_author()
            elif search == "Exit":
                continue
    except TypeError:
        _return()

def create_entry():
    while True:
        try:
            question = colored("How many books would you like to add? ", "blue", attrs=["bold"])
            how_many = int(input(question))
        except ValueError:
            cprint("Your answer must be a whole number.", "red", attrs=["bold"])
        else:
            break
    for item in range(how_many):
            cprint("Enter details for Book {}".format(item+1), "magenta", attrs=["bold"])
            b = Book()
            catalogue_objects.append(b.__dict__)
            cprint("Entry added.", "green", attrs=["bold"])
            _print_df(catalogue_objects)

def remove_entry():
    catalogue_list()
    question = colored("Leaving this section blank will return you to the main menu.\nSelect the entry to remove by typing in the corresponding number in the left-most column: ", "blue", attrs=["bold"])
    while True:
        try:
            remove_var = int(input(question))
            del catalogue_objects[remove_var]
            cprint("Entry has successfully been removed.", "green", attrs=["bold"])
            catalogue_list()
            break
        except IndexError: 
            cprint("Number not found, nothing has been removed.", "magenta", attrs=["bold"])
        except (ValueError, TypeError): 
            _return()
            break

def modify_entry():
    catalogue_list()
    question = colored("Leaving this section blank will return you to the main menu.\nSelect the entry to edit by typing in the corresponding number in the left-most column: ", "blue", attrs=["bold"])
    while True:
        try:
            edit_var = int(input(question))
            _print_df([catalogue_objects[edit_var]])
            modify = ""
            while modify != "Exit":
                modify = modify_menu()
                print(modify)
                if modify == "Title":
                    _update("title", "title", edit_var)
                    _print_df([catalogue_objects[edit_var]])
                elif modify == "Author":
                    _update("author", "author", edit_var)
                elif modify == "Price":
                    _update("price($)", "price", edit_var, float)
                    _print_df([catalogue_objects[edit_var]])
                elif modify == "Stock Count":
                    _update("stock", "stock_count", edit_var, int)
                    _print_df([catalogue_objects[edit_var]])
                elif modify == "Exit":
                    catalogue_list()
                    continue
                else:
                    cprint("Not a valid option, try again", "red", attrs=["bold"])
        except IndexError: 
            cprint("Number not found, unable to edit.", "magenta", attrs=["bold"])
        except (ValueError, TypeError): 
            _return()
            break


# main program
def main_program():
    init()
    tprint("welcome")
    cprint("Please remember that everything is case sensitive!", "red", attrs=["underline"])
    print("")
    option = ""
    try:
        while option != "Exit":
            option = main_menu()
            print(option)
            if option == "Catalogue list":
                catalogue_list()
            elif option == "Search catalogue":
                search_catalogue()
            elif option == "Create entry":
                create_entry()
            elif option == "Remove entry":
                remove_entry()
            elif option == "Modify entry":
                modify_entry()
            elif option == "Exit":
                continue
    except TypeError:
        tprint("goodbye")
        exit()
    tprint("goodbye")

# run main program
main_program()
