from dataclasses import dataclass
import datetime

@dataclass
class Author:
    name: str
    bio: str
    birth_date: datetime
    death_date: datetime
