# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("mike", 28)
# p2 = Person("joe", 28)
# p3 = Person("nick", 27)
# p4 = Person("Janet", 27)
# people = [p1, p2, p3]
# #need something like
# matches = getMatches(people, "age")
# print matches
# [[Mike's object, Joe' Object], [Nick's object, Janet's object]]

# from operator import attrgetter
# from itertools import groupby
# def getMatches(people, prop):
#     people = sorted(people, key = attrgetter(prop))
#     return [list(grp) for k, grp in groupby(people, attrgetter(prop))]

# print getMatches(people, "age")

# for group in getMatches(people, "age"):
#     print [people.name for people in group]

# class Book:
#     def __init__(self):
#         self.title = []
#         self.author = []
#         self.price = []
#         self.stock_count = []

#     def add_title(self, title):
#         self.title.append(title)

#     def add_author(self, author):
#         self.author.append(author)

#     def add_price(self, price):
#         self.price.append(price)

#     def add_stock_count(self, stock_count):
#         self.stock_count.append(stock_count)

#     def show_title(self):
#         return self.title

#     def show_author(self):
#         return self.author

#     def show_price(self):
#         return self.price

#     def show_stock_count(self):
#         return self.stock_count

# while True:
#     try:
#         how_many = int(input("How many books would you like to add? "))
#     except ValueError:
#         print("Your answer must be a whole number.")
#     else:
#         break

# x = Book()

# for item in range(how_many):
#         print("Enter details for Book {}".format(item+1))
#         x.add_title(input("Title: "))
#         x.add_author(input("Author: "))
#         while True:
#             try:
#                 x.add_price(float(input("Price (in $): ")))
#             except(ValueError): 
#                 print("This needs to be a number.")
#             else:
#                 break
#         while True:
#             try:
#                 x.add_stock_count(int(input("Stock count: ")))
#             except(ValueError): 
#                 print("This needs to be a number.")
#             else:
#                 break

# print(x.__dict__)
# print(x)

# class myStruct():
#     def __init__(self, name, salary, doB, title):
#         self.name = name
#         self.salary = salary
#         self.doB = doB
#         self.title = title


# name = input('Enter name: ')
# salary = input('Enter salary: ')
# doB = input('Enter doB: ')
# title = input('Enter title: ')

# new_object = myStruct(name, salary, doB, title)

# print(new_object.__dict__)

for x in test_list:
    if getattr(x, x.fieldMemberName) == value
        print("i found it!")
        break
else:
    x = None

