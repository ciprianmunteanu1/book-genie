from dataclasses import dataclass
from lib import Book, ReadingChallenge

@dataclass
class User:
    id: int
    name: str
    username: str
    email: str
    password: str
    profile_description: str
    profile_level: int

    preffered_genres: list
    wishlist: list[Book]
    
    reading_now: list[Book]
    reading_history: list[Book]
    read_last_year: list[Book]
    
    reading_challenge: list[ReadingChallenge]
