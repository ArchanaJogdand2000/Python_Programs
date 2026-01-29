# class BookStore 
# instance variables Name(Book name) and Author(Book Author)
# one Class variable --> NoOfBooks
#Display information of book 

class BookStore:
    NoOfBooks = 0
    def __init__(self,A,B):

        self.Name =  A
        self.Author = B
        BookStore.NoOfBooks =  BookStore.NoOfBooks + 1

    def Display(self):
        print(self.Name,"by",self.Author,". No of books :",BookStore.NoOfBooks)
        
obj1 = BookStore("Linux System programming", "Robert Love")
obj1.Display()

obj2 = BookStore("The C programming Lanquage", "Brian  Kernighan & Dennis  Ritchie")
obj2.Display()

obj3 =  BookStore("The C++ Programming Language","Bjarne Stroustrup")
obj3.Display()