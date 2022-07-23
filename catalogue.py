from book_class import Book
from tabulate import tabulate

class Catalogue():
    def __init__(self, book_list):
        self.book_list = book_list

    def add_cata(self):
        pass
        # adds book to catalogue list

    def rm_cata(self):
        # removes book from catalogue list
        pass

    def show_cata(self):
        pass
        # displays catalogue



r1 = Book("get fucked", "fuck off", 55, 50)

print(r1.__dict__)

table = [[r1["Sun",696000,1989100000],["Earth",6371,5973.6], ["Moon",1737,73.5],["Mars",3390,641.85]]
print(tabulate(table))

print(tabulate(table, headers=["Title","Author", "Price", "Stock count"]))

