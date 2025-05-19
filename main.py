from library_manager import *

library = Library()
library.add_book("Война и мир", "Толстой", "Роман")
library.add_book("Идиот", "Достоевский", "Роман")
library.print_all()
library.remove_book("Война и мир")
library.remove_book("Несуществующая книга")  
library.print_all()
