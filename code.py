title_list = []
author_list = []
price_list = []
stock_count_list = []

lists = [title_list, author_list, price_list, stock_count_list]
catalogue = []

Book.create_book("fuck you", "fuck off", 55, 51)
Book.create_book("fuck you", "fuck off", 55, 52)
Book.create_book("fuck you", "fuck off", 55, 53)

print(catalogue)
print(lists)


def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

    # def create_book(title, author, price, stock_count):
    #     x = input("What do you want to call this entry?")
    #     x = Book(title, author, price, stock_count)
    #     catalogue.append(x)
    #     title_list.append(title)
    #     author_list.append(author)
    #     price_list.append(price)
    #     stock_count_list.append(stock_count)
    #     return x