# Author class
class Author:

    def __init__(self, a_name, a_country, a_birthday, a_books):
        self.a_name = a_name
        self.a_country = a_country
        self.a_birthday = a_birthday
        self.a_books = a_books

    def __str__(self):
        return f"An instance of the {__class__.__name__} class with name {self.a_name}"

    def __repr__(self):
        return f"{self.a_name}"
    
    def __eq__(self, other):
        return self.a_name == other.a_name
    


a_1 = Author("Taras Shevchenko", "Ukraine", "09.03.1814", ["Kobzar"])
a_2 = Author("Erich M Remarque", "Germany", "22.06.1898", ["All Quiet on the Western Front"])


# Book class
class Book:

    amount_of_all_existing_books = 0

    def __init__(self, b_name, b_year, b_author: Author):

        Book.amount_of_all_existing_books += 1

        self.b_name = b_name
        self.b_year = b_year
        self.b_author = b_author

    @staticmethod
    def amount_of_books():
        return f"There are {Book.amount_of_all_existing_books} copies of Book class"

    def __str__(self):
        return f"An instance of the {__class__.__name__} class with name {self.b_name}"

    def __repr__(self):
        return f"{self.b_name}"
    
    def __eq__(self, other):
        return self.b_name == other.b_name


b_1 = Book("Kobzar", 1840, a_1)
b_2 = Book("All Quiet on the Western Front", 1928, a_2)


# The Library class
class Library:

    def __init__(self, l_name, l_books: list, l_authors: list):
        self.l_name = l_name
        self.l_books = l_books
        self.l_authors = l_authors

    def __str__(self):
        return f"An instance of the {__class__.__name__} class with name {self.l_name}"

    def __repr__(self):
        return f"{self.l_name}"

    def new_book(self, book_name, year, author_name, country, birthday):
        new_author = Author(author_name, country, birthday, [book_name])
        new_book = Book(book_name, year, new_author)
        for book in self.l_books:
            if book == new_book:
                print("This book is already in the library")
                break
        for author in self.l_authors:
            if book != new_book and author == new_author:
                author.a_books.append(new_book)
                self.l_books.append(new_book)
                break
            else:
                self.l_books.append(new_book)
                self.l_authors.append(new_author)
                break

    def group_by_author(self, author):
        books_list = []
        for item in self.l_authors:
            if item.a_name == author:
                books_list = item.a_books
                break
        if len(books_list) == 0:
            return "There are no books of this author"
        else:
            return f"Here are {author}'s books: {books_list}"

    def group_by_year(self, year):
        books_list = []
        for item in self.l_books:
            if item.b_year == year:
                books_list.append(item.b_name)
                break
        if len(books_list) == 0:
            return "There are no books written this year"
        else:
            return f"Here are the books that were written in {year}: {books_list}"


lib_1 = Library("Lib", [b_1, b_2], [a_1, a_2])

print(lib_1.l_books, lib_1.l_authors)

# Trying to add a new book
lib_1.new_book("Kobzar", 1840, "Taras Shevchenko", "Ukraine", "09.03.1814")
lib_1.new_book("The Dream", 1840, "Taras Shevchenko", "Ukraine", "09.03.1814")
lib_1.new_book("Pale Blue Dot", 1994, "Carl Sagan", "USA", "09.06.1834")
print(lib_1.l_books, lib_1.l_authors)

print(lib_1.group_by_author("Taras Shevchenko"))
print(lib_1.group_by_year(1994))

# Returns amount of all existing instances of the Book class
print(Book.amount_of_books())

