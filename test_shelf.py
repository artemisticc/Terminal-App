
# Example Python program to create an in-memory shelf

import shelve

import pickle


 

# Class definition

class Record():

     # Initialiser   

    def __init__(self, title, author, price, stock_count):
        self.title = title
        self.author = author
        self.price = price
        self.stock_count = stock_count

   

    def __repr__(self):

        return "Record>>id:%d, Name:%s, Contents:%s"%(self.id, self.name, self.contents);

       

r1 = Record("title1", "author1", 55, 50);

r2 = Record("title2", "author2", 56, 51);

 

d1 = {};

shelf = shelve.Shelf(d1);

 

# Python internally pickles the values

shelf["1"] = r1;

shelf["2"] = r2;

 

# Python internally unpickles the values

print(shelf["1"]);

print(shelf["2"]);