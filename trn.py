class Library:
    def __init__(self, name):
        self.name = name
        self.books = set()
        self.authors = set()

    def add_new_book(self, book):
        self.books.add(book)
        self.authors.add(book.author)

    def group_by_author(self, author):
        return [bk for bk in self.books if bk.author == author]

    def group_by_year(self, year):
        return [yr for yr in self.books if yr.year == year]

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name.upper()


class Book:
    books_count = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name.upper()


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = set()

    def write_new_book(self, name: str, year: int):
        Book.books_count += 1
        book = Book(name, year, self)
        self.books.add(book)
        return book

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name.upper()


cities_lib = Library('City Library')
name = Author('Name Namich', 'USA', '01/01/1960')

book_1 = name.write_new_book('BOOK_1', 2000)
book_2 = name.write_new_book('BOOK_2', 1987)
book_3 = name.write_new_book('BOOK_3', 2018)

cities_lib.add_new_book(book_1)
cities_lib.add_new_book(book_2)
cities_lib.add_new_book(book_3)

print(cities_lib.group_by_author(name))
