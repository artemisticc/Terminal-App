import sys
from book_class import Book
from simple_term_menu import TerminalMenu
from termcolor import colored, cprint
from tabulate import tabulate
from art import *
import pandas as pd

# with shelve.open('catalogue.db', '')
# main program

# global variables
# catalogue = [["Title","Author", "Price($)", "Stock"]]
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

def _index_list():
    return list(enumerate(catalogue_objects))

# functions for main features
def catalogue_list():
    df = pd.DataFrame(catalogue_objects)
    print(tabulate(df, headers=["Title","Author", "Price($)", "Stock"], tablefmt="fancy_grid"))
    # print(tabulate(catalogue, headers="firstrow", showindex="always", tablefmt="fancy_grid"))
    # print(catalogue_objects)

def _search_title():
    title_var = input("What title are you looking for? ")
    n = 0
    x = list(filter(lambda item: item["title"] == title_var, catalogue_objects))
    df = pd.DataFrame(x)
    for item in catalogue_objects:
        if item["title"] == title_var:
            n += 1
    if n == 1:
        cprint("There is " + str(n) + " book with this title in the system.", 'green', attrs=['bold'], file=sys.stderr)
        print(tabulate(df, headers=["Title","Author", "Price($)", "Stock"], tablefmt="fancy_grid"))
        return n
    elif n > 1:
        cprint("There are " + str(n) + " books with this title in the system.", 'green', attrs=['bold'], file=sys.stderr)
        print(tabulate(df, headers=["Title","Author", "Price($)", "Stock"], tablefmt="fancy_grid"))
        return n
    else:
        cprint("There are no books with this title in the system.", 'magenta', attrs=['bold'], file=sys.stderr)
        return n

def _search_author():
    question = colored("What author are you looking for? ", 'blue')
    author_var = input(question)
    n = 0
    x = list(filter(lambda item: item["author"] == author_var, catalogue_objects))
    df = pd.DataFrame(x)
    for item in catalogue_objects:
        if item["author"] == author_var:
            n += 1
    if n == 1:
        cprint("There is " + str(n) + " book with this author in the system.", 'green', attrs=['bold'], file=sys.stderr)
        print(tabulate(df, headers=["Title","Author", "Price($)", "Stock"], tablefmt="fancy_grid"))
    elif n > 1:
        cprint("There are " + str(n) + " books with this title in the system.", 'green', attrs=['bold'], file=sys.stderr)
        print(tabulate(df, headers=["Title","Author", "Price($)", "Stock"], tablefmt="fancy_grid"))
    else:
        cprint("There are no books with this author in the system.", 'magenta', attrs=['bold'], file=sys.stderr) 

def search_catalogue():
    search = ""
    while search != "Exit":
        search = search_menu()
        if search == "Title":
            _search_title()
        elif search == "Author":
            _search_author()
        elif search == "Exit":
            continue
        else:
            cprint("Not a valid option, try again.", 'red', attrs=['bold'], file=sys.stderr)


def create_entry():
    while True:
        try:
            how_many = int(input("How many books would you like to add? "))
        except ValueError:
            cprint("Your answer must be a whole number.", 'red', attrs=['bold'], file=sys.stderr)
        else:
            break

    for item in range(how_many):
            print("Enter details for Book {}".format(item+1))
            b = Book()
            # catalogue.append([b.title, b.author, b.price, b.stock_count])
            catalogue_objects.append(b.__dict__)
            # catalogue_actual_objects.append(b)
            print("Entry created. \n", b.__dict__)

def remove_entry():
    n = _search_title()
    if n > 1:
        input("Using the numbers on the left, which book would you like to remove from the system? ")
    elif n == 1:
        x = input("Do you want to permanently remove this book from the system? ")
        # if x 
    else:
        cprint("Nothing to remove.", "red", file=sys.stderr)




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
            cprint("Not a valid option, try again", 'red', attrs=['bold'], file=sys.stderr)


# main program

def main_program():
    tprint("welcome")
    cprint("Please remember that everything is case sensitive!", "red", attrs=["underline"], file=sys.stderr)
    print("")
    option = ""
    while option != "Exit":
            option = main_menu()
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
            else:
                cprint("Not a valid option, try again", 'red', attrs=['bold'], file=sys.stderr)

main_program()
tprint("goodbye")
_index_list()
print(_index_list())
