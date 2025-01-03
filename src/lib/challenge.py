from dataclasses import dataclass
import datetime
from lib.book import Book

@dataclass
class ReadingChallenge:
    created_at: datetime
    updated_at: datetime
    start_date: datetime
    end_date: datetime
    number_of_read_books: int
    read_books_list: list[Book]
    status: str
    reward_message: str