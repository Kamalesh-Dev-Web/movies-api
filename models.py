from beanie import Document
from pydantic import Field


class Movie(Document):
    title:str
    rating:str
    year:int
    description:str
    genre:list[str]
    
    class Settings:
        name="movies_database"
    
    class Config:
        schema_extra={
             "title":"Avengers",
             "rating":"9.0",
             "year":2001,
             "description":"A marvel movie",
             "genre":["action","thriller","larger than life"]
        }