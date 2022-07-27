from itertools import groupby
from operator import itemgetter
import pandas as pd
from tabulate import tabulate
from decimal import Decimal
from termcolor import colored, cprint
import sys
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

def test():
    edit_var=0
    title_var = input("Updated title: ")
    update_title = {"title": title_var}
    catalogue_objects[edit_var].update(update_title)
    author_var = input("Updated author: ")
    update_author = {"author": author_var}
    catalogue_objects[edit_var].update(update_author)
    price_var = input("Updated price($): ")
    update_price = {"price": price_var}
    catalogue_objects[edit_var].update(update_price)
    stock_var = input("Updated stock: ")
    update_stock = {"stock_count": stock_var}
    catalogue_objects[edit_var].update(update_stock)
    print(catalogue_objects)

def _return():
    cprint("Returning to main menu.", 'magenta', attrs=['bold'], file=sys.stderr)

def _failed(key1):
    cprint("Failed to update " + key1 + ".", 'red', attrs=['bold'], file=sys.stderr)

def _update(key1, key2, type=str):
        try:
            a = colored("Updated " + key1 + ": ", 'grey', attrs=['bold'])
            x = type(input(a))
            if not x:
                _failed(key1)
                return
            y = {key2: x}
            catalogue_objects[var].update(y)
        except ValueError:
            _failed(key1)
            return

def test2():
        _update("title", "title")
        _update("author", "author")
        _update("price($)", "price", float)
        _update("stock", "stock_count", int)
        print(catalogue_objects)



# # define a fuction for key
# # def sort_func(k):
# #     return k['author']

# # sort INFO data by 'author' key.
# my_var = input("what title: ")
# x = list(filter(lambda item: item['author'] == my_var, catalogue_objects))
# print(x)



# print(tabulate(df, headers="keys", tablefmt="fancy_grid"))

# del catalogue_objects[0]


