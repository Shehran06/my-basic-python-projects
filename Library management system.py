class book:

    def __init__(self, title, isbn, status=True):
        self.title= title
        self.isbn=isbn
        self.status=status

    def availability(self, available):
        self.status=available
        return f"The book is {'availabe' if available == True else 'not available'}"

class User:

    def __init__(self, name, user_id, borrowed_books=[]):
        self.name=name
        self.user_id=user_id
        self.borrowed_books=borrowed_books

    def borroowbook(self,book):
        self.borrowed_books.append(book)

    def returnbook(self, book):
        self.borrowed_books.remove(book)

    def viewborrowedbooks(self):
        return self.borrowed_books

class Library:
    def __init__(self,books=[],users=[]):
        self.books=books
        self.users=users

    def addabook(self, book):
        self.books.append(book)

    def search(self, booktitle):
        for i in self.books:#book class is automatically inherited in python to search each book in the list
            if booktitle == i:#if the title is found from the book class
                return i
            #return "cant find"

    def borrow(self, book):
        self.books.remove(book)

    def viewbooks(self):
        return self.books

book1= book("aaa", 1039485750,True)
print(book1.availability(False))

user1=User("aaa", 123, ["aaaa", "bbbb", "cccc"])
user1.borroowbook("dddddd")
print(user1.viewborrowedbooks())

Library1= Library(["a","bbbbb","ccccc"], ["user1","user2","user3"])
Library1.addabook(book1.title)
print(Library1.viewbooks())
print(Library1.search("aaa"))