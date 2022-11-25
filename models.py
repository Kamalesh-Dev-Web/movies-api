from beanie import Document
from pydantic import Field,BaseModel
from typing import Union,Optional


class Movie(Document):
    title:Union[str, None]=Field(max_length=400)
    rating:Union[str, None]=Field(max_length=400)
    year:Union[int, None]
    description:Union[str, None]=Field(max_length=400)
    genre:Union[list[str], None]
    
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
        
        
class UpdateMovie(BaseModel):
    rating:Optional[str]=None
    year:Optional[int]=None
    description:Optional[str]=None
    genre:Optional[list[str]]=None