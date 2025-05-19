# library_manager/utils/formatting.py

def format_book_data(data: dict) -> str:
    return f'Название "{data.get('name')}",  автор "{data.get('author')}",  жанр "{data.get('genre')}"'    
    
