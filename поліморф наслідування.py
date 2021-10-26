class Author:
    def __init__(self, name, country, birthday, books = set()):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books
        
    def write_new_book(self,name: str, year: int):
        
        for i in self.books:
            if name == i.name and year == i.year:
                raise TypeError('Така книга вже існує')
            book = Book(name,year, self)
            self.books.add(book)
            Book.books_count += 1
            #breakpoint()
            return book
    
    def __str__(self):
        return f"{self.name} ({self.country}, {self.birthday})"
    def __repr__(self):
        return f"Object of class Author with attributes {self.__dict__}"
    def __eq__(self, other):
        return ((self.name == other.name) and (self.country == other.country) and (self.birthday == other.birthday))
    def __hash__(self):
        return hash((self.name,self.country,self.birthday))


class Book:
    books_count = 0
    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
    def __str__(self):
        return f"Welcome! I'm a book name {self.name}. I was written in {self.year} by {self.author.name}."
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return ((self.name == other.name) and (self.year == other.year) and (self.author == other.author))
    def __hash__(self):
        return hash((self.name,self.year,self.author))
    
    
class Library:
    def __init__(self, name, books = set(), authors = set()):
        self.name = name
        self.books = books
        self.authors = authors
        
    def add_new_book(self,book: Book):
        self.books.add(book)
        
        self.authors.add(book.author)
    def group_by_author(self,author: Author):
        return list(author.books)
    
    def group_by_year(self,year: int):
        return list(x for x in self.books if x.year == year)
    
    def __str__(self):
        return f"Hello there. This library's name is {self.name}.\n Check all the books: {str(x.name for x in self.books)}.\nAll the authors: {str(x.name for x in self.authors)}\n"
    
    def __repr__(self):
        return self.__str__()


    
lib1 = Library ('Top Library')
a1 = Author('John', 'Mongolia',1999)
print(a1.__repr__())
print(a1.__str__())

a1.write_new_book('test', 2020)
print(a1.__repr__())
print(a1.__str__())


a1.write_new_book('test', 2020)
print(a1.__repr__())
print(a1.__str__())

a1.write_new_book('another book', 1999)
print(a1.__repr__())
print(a1.__str__())

a2 = Author('Michael', 'Zimbabwe', 1975)
a2.write_new_book('Magic Tales', 2020)
l = list(a1.books)
print(l)

for i in l:
    lib1.add_new_book(i)
print(lib1.group_by_year(2020))

