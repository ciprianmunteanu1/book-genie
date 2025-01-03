from dataclasses import dataclass
import datetime
from lib.author import Author

@dataclass
class Book:
    isbn: int
    author: Author
    
    genre: str
    book_description: str
    number_of_pages: int
    date_published: datetime
    global_rating: float
    
    added_by_user: datetime
    finished_by_user: datetime
    user_shelf: str
    user_rating: float
