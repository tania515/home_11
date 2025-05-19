# library_manager/utils/data_validation.py

def validate_book_data(data: dict) -> bool:
    if (data.get('name')!= None and data.get('author')!= None and data.get('genre')!= None):
        return True
    else: return False
    
    
    