## IMPORTS
from scoop import Scoop
#-------------------------MAIN TASK--------------------------------------------
"""
In the previous
exercise, we created a Scoop class that represents one scoop of ice cream. If
we’re really going to model the real world, though, we should have another object
into which we can put the scoops. I thus want you to create a Bowl class,
representing a bowl into which we can put our ice cream
"""
class Bowl:
    def __init__(self): self.scoops = []
    def add_scoop(self, *args): self.scoops.extend(list(args))
    def remove_scoop(self, r_scoop):
        flavours = [s.getFlavour() for s in self.scoops]
        if not (r_scoop in flavours):
            print(f'Bowl does not have flavour <{r_scoop}>')
        else:
            self.scoops.pop(flavours.index(r_scoop))

    def __str__(self):
        return 'Bowl is Empty' if not self.scoops else 'Bowl with flavour(s): '.upper() + ','.join([s.getFlavour() for s in self.scoops])


def test_bowl():
    s1, s2, s3 = Scoop(), Scoop('Choco'), Scoop('strawbery')
    b = Bowl()
    print(b)
    b.add_scoop(s1)
    print(b)
    b.add_scoop(s3)
    print(b)
    b.remove_scoop('bread')
    b.add_scoop(s2)
    print(b)
    b.remove_scoop('Choco')
    print(b)
#-------------------------BEYOND THE TASK--------------------------------------
"""
Create a Book class that lets you create books with a title, author, and price.
Then create a Shelf class, onto which you can place one or more books with an
add_book method. Finally, add a total_price method to the Shelf class, which
will total the prices of the books on the shelf.
"""
class Book:
    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width
    def __str__(self): return f'Book name: {self.title},\n author: {self.author},\n price: {self.price}'
    def __repr__(self): return f'Book name: {self.title},\n author: {self.author},\n price: {self.price}'
    def getTitle(self): return self.title
    def getAuthor(self): return self.author
    def getPrice(self): return self.price
    def getWidth(self): return self.width
    # --------------------------------
    def setTitle(self, title): pass
    def setAuthor(self, aurthor): pass
    def setPrice(self, price): pass


class Shelf:
    def __init__(self, width):
        self.books = []
        self.width = width
    def __str__(self): return f'Shelf has {len(self.books)} books. Total price: {self.total_price()}'
    def add_book(self, *books):
        for book in books:
            self.books.append(book)
            if self.getCurrentWidth() > self.width: raise Exception('Shelf max width exceeded')
    def remove_book(self, book):
        r_books = [b.getTitle() for b in self.books]
        if not (book in r_books): print(f'Book <{book}> is NOT on the shelf')
        else:
            print(f'Book <{book}> taken from the shelf')
            self.books.pop(r_books.index(book))
    def getCurrentWidth(self): return sum(b.getWidth() for b in self.books)
    def total_price(self): return sum(b.getPrice() for b in self.books)
    def has_book(self, book): return book in (b.getTitle() for b in self.books)
    def show_books(self):
        for b in self.books: print(b, end='\n---------\n')

def test_books_shelfs():
    from random import randint
    b1, b2, b3, b4 = Book('T1','A1',randint(1,53), randint(1,5)), Book('T2','A2',randint(1,53), randint(1,5)), \
    Book('T3','A3',randint(1,53), randint(1,5)), Book('T4','A4',randint(1,53), randint(1,5))
    sh = Shelf(7)
    print(sh)
    print(sh.has_book('T3'))
    sh.add_book(b2,b3)
    print(sh.has_book('T3'))
    print(sh)
    sh.show_books()
    sh.remove_book('T1')
    sh.remove_book('T2')
    print(sh)

"""
Write a method, Shelf.has_book, that takes a single string argument and
returns True or False, depending on whether a book with the named title
exists on the shelf.
"""
# Added method is in the class Shelf

"""
 Modify your Book class such that it adds another attribute, width. Then add a
width attribute to each instance of Shelf. When add_book tries to add books
whose combined widths will be too much for the shelf, raise an exception.
"""
# Added method is in the class Shelf


if __name__ == '__main__':
    test_books_shelfs()
    # test_bowl()
