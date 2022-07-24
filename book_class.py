class Book():
    def __init__(self, title = None, author = None, price = None, stock_count = None):
        if not title:
            while True:
                try:
                    self.title = input("Title: ")
                    if not self.title:
                        raise ValueError("empty")
                except ValueError: 
                    print("This can't be left blank.")
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
                    print("This can't be left blank.")
                else:
                    break
        else:
            self.author = author
        if not price:
            while True:
                    try:
                        self.price = float(input("Price: "))
                    except(ValueError): 
                        print("This needs to be a number.")
                    else:
                        break
        else:
            self.price = price
        if not stock_count:
            while True:
                try:
                    self.stock_count = int(input("Stock count: "))
                except(ValueError): 
                    print("This needs to be a number.")
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

    # def set_title(self, title, title_value):
    #     setattr(self, title, title_value)

    # def set_author(self, author, author_value):
    #     setattr(self, author, author_value)

    # def set_price(self, price, price_value):
    #     setattr(self, price, price_value)

    # def set_stock(self, stock_count, stock_value):
    #     setattr(self, stock_count, stock_value)

# def add_book(title, author, price, stock_count):
#     title = input("Title: ")
#     author = input("Author: ")
#     price = float(input("Price (in $): "))
#     stock_count = int(input("Stock count: "))
#     new_book = Book(title, author, price, stock_count)

# b = Book()
# print(b.__dict__)