"""
class Library:
    pass


class Book:
    pass


class Author:
    pass
"""


class Library:
    def __init__(self, name):
        # if not isinstance(name, str):
        #     raise TypeError(f"Недопустимий тип для {name}")
        self.name = name
        self.books = set()
        self.authors = set()

    def add_new_book(self, nbook):
        """
        додає книгу до списку книг поточної бібліотеки
        :param nbook:Book
        """
        # new_book = (book.name, book.year, book.author)
        # if new_book in self.books:
        #     raise ValueError("Така книга вже є")
        self.books.add(nbook)
        if nbook.author not in self.authors:
            self.authors.add(nbook.author)

    def group_by_author(self, author):
        """
        повертає список усіх книг за заданим автором
        :param author:Author
        :return: list
        """
        # if not isinstance(author, Author):
        #     raise TypeError
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        """
        повертає список усіх книг за заданим роком
        :param year:int
        :return: list
        """
        # if not isinstance(year, int):
        #     raise TypeError(f"Недопустимий тип для {int}")
        return[book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Object of class Library with attributes {self.__dict__}"

    def __str__(self):
        return f"Library {self.name} with {len(self.books)} books of {len(self.authors)} authors"


class Book:
    books_count = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f"Object of class Book with attributes {self.__dict__}"

    def __str__(self):
        return f'"{self.name}" - {self.author.name}, {self.year} №.{Book.books_count}'

    def __eq__(self, other):
        return self.name == other.name and self.year == other.year \
               and self.author.name == other.author.name \
               and self.author.country == other.author.country and self.author.birthday == other.author.birthday

    def __hash__(self):
        return hash((self.name, self.year, self.author.name, self.author.country, self.author.birthday))


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = set()

    def write_new_book(self, name, year):
        """
        метод для добавлення нової книги в список книг автора з поверненням об'єкту класу Book
        :param name:str
        :param year:int
        :return: book:Book
        """
        # if not isinstance(name, str) or not isinstance(year, int):
        #     raise TypeError
        for b in self.books:
            if name == b.name and year == b.year:
                raise ValueError("Книга вже написана")
        new_book = Book(name, year, self)
        self.books.add(new_book)
        Book.books_count += 1

        # print(new_book)
        return new_book

    def __repr__(self):
        return f"Object of class Author with attributes {self.__dict__}"

    def __str__(self):
        return f"{self.name} ({self.country}, {self.birthday})"

    def __eq__(self, other):
        return self.name == other.name and self.country == other.country and self.birthday == other.birthday

    def __hash__(self):
        return hash((self.name, self.country, self.birthday))

'''		
	def write_new_book(self,name: str, year: int):
			book = Book(name,year, self)
			if book in self.books:
				print('Така книга вже існує')
			else:
				self.books.add(book)
				Book.books_count += 1
				#breakpoint()
				return book
'''


lib1 = Library("Central")
a1 = Author("Роджер Желязни", "США", "13.05.37")
a2 = Author("Стівен", "Кінг", "21.09.47")
a3 = Author("Анджей Сапковський", "Польща", "21.06.46")
lib1.add_new_book(a1.write_new_book("Бог світла", 1967))
# lib1.add_new_book(a1.write_new_book("Бог світла", 1967))
lib1.add_new_book(a1.write_new_book("Хроніки Амбера", 1986))   # 70
lib1.add_new_book(a1.write_new_book("Джек із тіні", 1971))
lib1.add_new_book(a2.write_new_book("Томмінокери", 1986))    # 87
lib1.add_new_book(a2.write_new_book("Темна вежа", 1982))
lib1.add_new_book(a2.write_new_book("Воно", 1986))
lib1.add_new_book(a3.write_new_book("Останнє бажання", 1990))
lib1.add_new_book(a3.write_new_book("Час погорди", 1995))


print(lib1)
# lib1.print_select("ga")
print("=================== 1986 ===============================")
for book in lib1.group_by_year(1986):
    print(book)

# print([book for book in self.books if book[2] == author])
# tmp = []
# for book in self.books:
#     if book[2] == author:
#         tmp.append(book)
# print(tmp)
'''
    def print_select(self, choice=""):
        if choice == "b":
            for book in self.books:
                print(f"{book[0]} - {book[2]}, {book[1]}")
        elif choice == "a":
            for author in self.authors:
                print(author)
        elif choice == "ga":
            for author in self.authors:
                print("-----------", author)
                for book in self.group_by_author(author):
                    print(book)
        else:
            print("Books:")
            for book in self.books:
                print(f"{book[0]} - {book[2]}, {book[1]}")
            print("Authors:")
            for author in self.authors:
                print(author)
'''