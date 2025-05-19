# library_manager/catalog.py

from .customException import MyCustomException, BookNotFoundError, BookAlreadyExistsError
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
        for i in range(len(self.__books)):
            print(self.__books[i])
        
        
  
        
    
    
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