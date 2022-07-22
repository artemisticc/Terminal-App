class BookItem():

    def __init__(self, title, author, genre, price, stock_count):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stock_count = stock_count

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre

    def set_stock():
        pass

book1 = BookItem("My book", "Nicole Hall", "Self help", 40, 30)

# print(book1.__dict__)
print(BookItem.__module__)