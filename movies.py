from fastapi import APIRouter
from models import Movie
from typing import List

movies_router=APIRouter()

@movies_router.get('/')
async def getallmovies() -> List[Movie]:
    movies= await Movie.find_all().to_list()
    return movies

@movies_router.post('/')
async def createmovie():
    pass

@movies_router.get('/{movie_id}')
async def getmovie(movie):
    pass

@movies_router.put('/{movie_id}')
async def updatemovie(movie):
    pass

@movies_router.delete('/{movie_id}')
async def getallmovies():
    pass