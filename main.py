import sys
from book_class import Book
from simple_term_menu import TerminalMenu
from termcolor import colored, cprint
from tabulate import tabulate
from art import *
import pandas as pd
from colorama import init


catalogue_objects = []

def main_menu():
    cprint("What would you like to do?", "blue", attrs=['bold'], file=sys.stderr)
    options = ["Catalogue list", "Search catalogue", "Create entry", "Remove entry", "Modify entry", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    option = options[menu_entry_index]
    return option

def modify_menu():
    cprint("What would you like to modify about this entry?", "blue", attrs=['bold'], file=sys.stderr)
    modify_options = ["Title", "Author", "Price", "Stock Count", "Exit"]
    terminal_menu = TerminalMenu(modify_options)
    menu_entry_index = terminal_menu.show()
    option = modify_options[menu_entry_index]
    return option

def search_menu():
    cprint("What would you like to search by?", "blue", attrs=['bold'], file=sys.stderr)
    modify_options = ["Title", "Author", "Exit"]
    terminal_menu = TerminalMenu(modify_options)
    menu_entry_index = terminal_menu.show()
    option = modify_options[menu_entry_index]
    return option

def _return():
    cprint("Returning to main menu.", 'magenta', attrs=['bold'], file=sys.stderr)

def _print_df(var):
    df = pd.DataFrame(var)
    print(tabulate(df, headers=["Title","Author", "Price($)", "Stock"], tablefmt="fancy_grid"))

def _search_title():
    question = colored("What title are you looking for? ", 'blue', attrs=["bold"])
    title_var = input(question)
    n = 0
    x = list(filter(lambda item: item["title"] == title_var, catalogue_objects))
    for item in catalogue_objects:
        if item["title"] == title_var:
            n += 1
    if n == 1:
        cprint("There is " + str(n) + " book with this title in the system.", 'green', attrs=['bold'], file=sys.stderr)
        _print_df(x)
        return n
    elif n > 1:
        cprint("There are " + str(n) + " books with this title in the system.", 'green', attrs=['bold'], file=sys.stderr)
        _print_df(x)
        return n
    else:
        cprint("There are no books with this title in the system.", 'magenta', attrs=['bold'], file=sys.stderr)
        return n

def _search_author():
    question = colored("What author are you looking for? ", 'blue', attrs=['bold'])
    author_var = input(question)
    n = 0
    x = list(filter(lambda item: item["author"] == author_var, catalogue_objects))
    for item in catalogue_objects:
        if item["author"] == author_var:
            n += 1
    if n == 1:
        cprint("There is " + str(n) + " book with this author in the system.", 'green', attrs=['bold'], file=sys.stderr)
        _print_df(x)
    elif n > 1:
        cprint("There are " + str(n) + " books with this title in the system.", 'green', attrs=['bold'], file=sys.stderr)
        _print_df(x)
    else:
        cprint("There are no books with this author in the system.", 'magenta', attrs=['bold'], file=sys.stderr) 


# functions for main features
def catalogue_list():
    tprint("catalogue")
    df = pd.DataFrame(catalogue_objects)
    print(tabulate(df, headers=["Title","Author", "Price($)", "Stock"], tablefmt="fancy_grid"))


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
            how_many = int(input("How many books would you like to add? "))
        except ValueError:
            cprint("Your answer must be a whole number.", 'red', attrs=['bold'], file=sys.stderr)
        else:
            break

    for item in range(how_many):
            cprint("Enter details for Book {}".format(item+1), "blue", attrs=["bold"])
            b = Book()
            catalogue_objects.append(b.__dict__)
            print("Entry created. \n")
            _print_df(catalogue_objects)

def remove_entry():
    catalogue_list()
    question = colored("Select the entry to remove by typing in the corresponding number in the left-most column: ", 'blue', attrs=['bold'])
    while True:
        try:
            remove_var = int(input(question))
            del catalogue_objects[remove_var]
            cprint("Entry has successfully been removed.", "green", attrs=['bold'], file=sys.stderr)
            catalogue_list()
            break
        except IndexError: 
            cprint("Number not found, nothing has been removed.\nLeave space blank if you wish to return to the main menu.", 'magenta', attrs=['bold'], file=sys.stderr)
        except (ValueError, TypeError): 
            _return()
            break


def modify_entry():
    catalogue_list()
    question = colored("Select the entry to edit by typing in the corresponding number in the left-most column: ", 'blue', attrs=['bold'])
    while True:
        try:
            edit_var = int(input(question))
            print(catalogue_objects[edit_var])
            modify = ""
            while modify != "Exit":
                modify = modify_menu()
                print(modify)
                if modify == "Title":
                    title_var = input("Updated title: ")
                    update_title = {"title": title_var}
                    catalogue_objects[edit_var].update(update_title)
                elif modify == "Author":
                    author_var = input("Updated author: ")
                    update_author = {"author": author_var}
                    catalogue_objects[edit_var].update(update_author)
                elif modify == "Price":
                    price_var = input("Updated price($): ")
                    update_price = {"price": price_var}
                    catalogue_objects[edit_var].update(update_price)
                elif modify == "Stock Count":
                    stock_var = input("Updated stock: ")
                    update_stock = {"stock_count": stock_var}
                    catalogue_objects[edit_var].update(update_stock)
                elif modify == "Exit":
                    catalogue_list()
                    continue
                else:
                    cprint("Not a valid option, try again", 'red', attrs=['bold'], file=sys.stderr)
        except IndexError: 
            cprint("Number not found, unable to edit.\nLeave space blank if you wish to return to the main menu.", 'magenta', attrs=['bold'], file=sys.stderr)
        except (ValueError, TypeError): 
            _return()
            break


# main program

def main_program():
    init()
    tprint("welcome")
    cprint("Please remember that everything is case sensitive!", "red", attrs=["underline"], file=sys.stderr)
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


main_program()

# _index_list()
# print(_index_list())
