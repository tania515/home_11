class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        
        
    def __str__(self):
        return self.message
    
    
class BookNotFoundError(MyCustomException):
    def __init__(self, message):
        super().__init__(message)
        
        
class BookAlreadyExistsError(MyCustomException):
    def __init__(self, message):
        super().__init__(message)
       