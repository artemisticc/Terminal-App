from itertools import groupby
from book_class import Book
from catalogue import Catalogue
from simple_term_menu import TerminalMenu
from os import system
import shelve

# with shelve.open('catalogue.db', '')
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

def catalogue_list():
    pass

def search_catalogue():
    pass

def create_entry():
    x = Book()
    while True:
        try:
            how_many = int(input("How many books would you like to add? "))
        except ValueError:
            print("Your answer must be a whole number.")
        else:
            break

    for item in range(how_many):
            print("Enter details for Book {}".format(item+1))
            x.add_title(input("Title: "))
            x.add_author(input("Author: "))
            while True:
                try:
                    x.add_price(float(input("Price (in $): ")))
                except(ValueError): 
                    print("This needs to be a number.")
                else:
                    break
            while True:
                try:
                    x.add_stock_count(int(input("Stock count: ")))
                except(ValueError): 
                    print("This needs to be a number.")
                else:
                    break


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




def main_progam():
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
                print("I don't know how you managed to pick something that doesn't exist, but it's not valid, so try again")

print("Success!")
# my_data_file.close()
# save to json file here


