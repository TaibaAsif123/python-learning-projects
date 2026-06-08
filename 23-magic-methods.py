
"""
This program demonstrates dunder methods (__init__, __str__, __eq__, __lt__, __add__, 
__contains__, __getitem__) that define object behavior for comparison, string representation,
addition, membership testing, and indexing operations
"""

#=Dunder methods (double underscore) __init__,__str__,
#Automatically called by py built-in operations
#define behaviour of objects
class Book:
    def __init__(self,title,author,num_pg):
        self.title=title
        self.author=author
        self.num_pg=num_pg
    #customized printing object
    #it was printing address first
    #string representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __eq__(self, other) -> bool:
        return self.title==other.title and self.author==other.author
    #your own dunder method
    def __lt__ (self,other):
       return self.num_pg<other.num_pg
    def __add__(self,other):
        return self.num_pg+other.num_pg

    def __contains__ (self,keyword):
        return keyword in self.title
    def __getitem__(self,key):
        if key=="title":
            return self.title

#automatically called
book1=Book("The Hobbit","J.R.R.Tolkian",310)
book4=Book("The Hobbit","J.R.R.Tolkian",320)
book2=Book("Harry Potter","J.K Rowling",223)
book3=Book("The Lion","Lewis",172)
print (book1)
print(book1==book2) #what if they have same 2 but diff num of pages
print(book1==book4)
print(book2<book3)
print(book2+book3)
print("lion" in book3)
print(book3["title"])
