from itertools import groupby
from book_class import Book
from simple_term_menu import TerminalMenu
from os import system
import shelve
from tabulate import tabulate

# with shelve.open('catalogue.db', '')
# main program


def main_menu():
    print("What would you like to do?")
    options = ["Catalogue list", "Search catalogue", "Create entry", "Remove entry", "Modify entry", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    option = options[menu_entry_index]
    return option

def modify_menu():
    print("What would you like to modify about this entry?")
    modify_options = ["Title", "Author", "Price", "Stock Count", "Exit"]
    terminal_menu = TerminalMenu(modify_options)
    menu_entry_index = terminal_menu.show()
    option = modify_options[menu_entry_index]
    return option

def search_menu():
    print("What would you like to search by?")
    modify_options = ["Title", "Author", "Exit"]
    terminal_menu = TerminalMenu(modify_options)
    menu_entry_index = terminal_menu.show()
    option = modify_options[menu_entry_index]
    return option

catalogue = [["Title","Author", "Price($)", "Stock"]]
catalogue_objects = []
catalogue_actual_objects = []
list_of_matching_titles = [["Title","Author", "Price($)", "Stock"]]

def catalogue_list():
    print(tabulate(catalogue, headers='firstrow', showindex='always', tablefmt='fancy_grid'))
    print(catalogue_objects)
    _index_list()
    print(_index_list())

def _index_list():
    return list(enumerate(catalogue_objects))

def _search_title():
    title_var = input("What title are you looking for? ")
    n = 0
    for item in catalogue_objects:
        if item["title"] == title_var:
            n += 1
    if n == 1:
        print("There is " + str(n) + " book with this title in the system.")
    else:
        print("There are " + str(n) + " books with this title in the system.")

def _search_author():
    author_var = input("What author are you looking for? ")
    n = 0
    for item in catalogue_objects:
        if item["author"] == author_var:
            n += 1
    print("There are " + str(n) + " books with this author in the system.")

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
            print("Not a valid option, try again")


def create_entry():
    while True:
        try:
            how_many = int(input("How many books would you like to add? "))
        except ValueError:
            print("Your answer must be a whole number.")
        else:
            break

    for item in range(how_many):
            print("Enter details for Book {}".format(item+1))
            b = Book()
            catalogue.append([b.title, b.author, b.price, b.stock_count])
            catalogue_objects.append(b.__dict__)
            catalogue_actual_objects.append(b)
            print("Entry created. \n", b.__dict__)



def remove_entry():
    pass
# what is the title of the book you would like to remove
# check objects for matching attribute
# remove from catalogue?
# delete object



def modify_entry():
    modify = ""
    while modify != "Exit":
        search_catalogue()
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




def main_program():
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

main_program()
print("Success!")
# my_data_file.close()
# save to json file here


