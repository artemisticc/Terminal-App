class Book():

    def __init__(self, title, author, price, stock_count):
        self.title = title
        self.author = author
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

    def create_book(title, author, price, stock_count):
        book = Book(title, author, price, stock_count)
        return book