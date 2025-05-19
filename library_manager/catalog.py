# library_manager/catalog.py

from .customException import MyCustomException, BookNotFoundError, BookAlreadyExistsError
from .utils.data_validation import validate_book_data
from .utils.formatting import format_book_data
class Library:
    
    
    def __init__(self):
        self.__books = []
    
    def add_book(self, name, author, genre):
        self.__books.append(Book(name, author, genre))
    
    def remove_book(self, name):
        try:
            index = next ((i for i, b in enumerate(self.__books) if b.name == name), None)
            if index == None:
                raise BookNotFoundError(f"Книга {name} не найдена")
            else:
                del self.__books[index]
        except BookNotFoundError as e:
            print(e) 
            
    def print_all(self):
        if not self.__books:
            print("В библиотеке нет книг")
        else:
            for book in self.__books:          
                print(book)
                
    def print_report(self):
        if not self.__books:
            print("В библиотеке нет книг")
        else:
            for book in self.__books:
                book_data = {"name": book.name, "author": book.author, "genre": book.genre}
                if validate_book_data(book_data):
                    print(format_book_data(book_data))

            
    def found_book(self,name, author=None, genre=None):
        try:
            for i, book in enumerate(self.__books):
                if (book.name == name) and (author is None or book.author == author) and (genre is None or book.genre == genre):
                    print(f'Номер в каталоге: {i}')
                    return book
            else:
                raise BookNotFoundError(
                    f"Книга не найдена по параметрам: "
                    f"{'' 'название='+name} "
                    f"{'' if author is None else 'автор='+author} "
                    f"{'' if genre is None else 'жанр='+genre}"
                    )
        except BookNotFoundError as e:
            print(e) 
        
        
class Book:
    def __init__(self, name, author, genre):
        self.__name = name
        self.__author = author
        self.__genre =genre
        
        
    def __str__(self):
        return f'Название {self.__name},  автор {self.__author},  жанр {self.__genre}'
    
    @property
    def name(self):
        return self.__name
    
    @property
    def author(self):
        return self.__author
    
    @property
    def genre(self):
        return self.__genre
        
    @name.setter
    def name(self,name):
        self.__name = name
        
    @author.setter
    def author(self,author):
        self.__author = author
        
    @genre.setter
    def genre(self,genre):
        self.__genre = genre   