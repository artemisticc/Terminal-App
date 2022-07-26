import sys
from termcolor import cprint, colored

class Book():
    def __init__(self, title = None, author = None, price = None, stock_count = None):
        if not title:
            while True:
                try:
                    x = colored("Title: ", 'grey', attrs=['bold'])
                    self.title = input(x)
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
                    x = colored("Author: ", 'grey', attrs=['bold'])
                    self.author = input(x)
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
                        x = colored("Price($): ", 'grey', attrs=['bold'])
                        self.price = float(input(x))
                    except ValueError: 
                        cprint("This needs to be a number.", 'red', attrs=['bold'], file=sys.stderr)
                    else:
                        break
        else:
            self.price = price
        if not stock_count:
            while True:
                try:
                    x = colored("Stock count: ", 'grey', attrs=['bold'])
                    self.stock_count = int(input(x))
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

