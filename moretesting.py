from itertools import groupby
from operator import itemgetter
import pandas as pd
from tabulate import tabulate
from decimal import Decimal
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

board_dict = {
    'Done': {
        'point': 0.0,
        'items': 1
    },
    'Doing': {
        'point': 24.0,
        'items': 3
    },
    'New': {
        'point': 0.0,
        'items': 2
    },
    'Stuck': {
        'point': 19.0,
        'items': 3
    },
    'Ready to Test': {
        'point': Decimal('1'),
        'items': 1
    }
}

df = pd.DataFrame(catalogue_objects)
print(tabulate(df, headers="keys", tablefmt="fancy_grid"))