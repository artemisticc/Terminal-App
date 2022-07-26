import sys
from termcolor import cprint

class Book():
    def __init__(self, title = None, author = None, price = None, stock_count = None):
        if not title:
            while True:
                try:
                    self.title = input("Title: ")
                    if not self.title:
                        raise ValueError("empty")
                except ValueError: 
                    cprint("This can't be left blank.", 'red', attrs=['bold'], file=sys.stderr)
                else:
                    break
        else:
            self.title = title
        if not author:
            while True:
                try:
                    self.author = input("Author: ")
                    if not self.author:
                        raise ValueError("empty")
                except ValueError: 
                    cprint("This can't be left blank.", 'red', attrs=['bold'], file=sys.stderr)
                else:
                    break
        else:
            self.author = author
        if not price:
            while True:
                    try:
                        self.price = float(input("Price($): "))
                    except ValueError: 
                        cprint("This needs to be a number.", 'red', attrs=['bold'], file=sys.stderr)
                    else:
                        break
        else:
            self.price = price
        if not stock_count:
            while True:
                try:
                    self.stock_count = int(input("Stock count: "))
                except ValueError: 
                    cprint("This needs to be a number.", 'red', attrs=['bold'], file=sys.stderr)
                else:
                    break
        else:
            self.stock_count = stock_count

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock_count

