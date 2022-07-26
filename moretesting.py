from itertools import groupby
from operator import itemgetter
import pandas as pd
from tabulate import tabulate
from decimal import Decimal
from termcolor import colored, cprint
# dictionary
catalogue_objects = [
    {'title': 'book_1', 'author': 'beck', 'x': 'y_1'},
    {'title': 'book_2', 'author': 'hill', 'x': 'y_1'},
    {'title': 'book_3', 'author': 'anh', 'x': 'y_1'},
    {'title': 'book_4', 'author': 'anh', 'x': 'y_1'},
    {'title': 'book_5', 'author': 'hill', 'x': 'y_1'},
    {'title': 'book_6', 'author': 'anh', 'x': 'y_1'},
    {'title': 'book_7', 'author': 'beck', 'x': 'y_1'},
    {'title': 'book_8', 'author': 'hill', 'x': 'y_1'},
    {'title': 'book_9', 'author': 'beck', 'x': 'y_1'}
]


# # define a fuction for key
# # def sort_func(k):
# #     return k['author']

# # sort INFO data by 'author' key.
# my_var = input("what title: ")
# x = list(filter(lambda item: item['author'] == my_var, catalogue_objects))
# print(x)



# print(tabulate(df, headers="keys", tablefmt="fancy_grid"))

# del catalogue_objects[0]


def update():
    title_var = input("Updated title: ")
    update_title = {"title": title_var}
    catalogue_objects[0].update(update_title)

def print_df(var):
    df = pd.DataFrame(var)
    print(tabulate(df, headers=["Title","Author", "Price($)", "Stock"], tablefmt="fancy_grid"))

# df = pd.DataFrame(catalogue_objects)
cprint("Which book would you like to edit?", "green")
create_df()

update()
cprint("Entry updated successfully", "green")
create_df()



