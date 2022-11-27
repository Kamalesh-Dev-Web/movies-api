from fastapi import APIRouter,HTTPException
from models import Movie,UpdateMovie
from typing import List,Union
from beanie import PydanticObjectId

movies_router=APIRouter()

@movies_router.get('/')
async def getallmovies(title:Union[str, None] = None) -> List[Movie]:
    searched_results= await Movie.find(Movie.title==title).to_list()
    if title==None:
       movies= await Movie.find_all().to_list()
       return movies
    else: return searched_results
       
   

@movies_router.post('/')
async def createmovie(movie:Movie):
    await movie.create()
    
    return movie

@movies_router.get('/{movie_id}')
async def getmovie(movie_id:PydanticObjectId) -> Movie:
    result=await Movie.get(movie_id)
    return result

@movies_router.put('/{movie_id}')
async def updatemovie(movie:UpdateMovie,movie_id:PydanticObjectId) -> Movie:
    print (movie)
    result= await Movie.get(movie_id)
    print (result)
    if not result:
        raise HTTPException(status_code=404,detail='Item not found')
    
    if movie.year!=None:
       result.year=movie.year
    if movie.rating!=None:
       result.rating=movie.rating
    if movie.image_url!=None:
       result.image_url=movie.image_url
    if movie.thumbnail!=None:
       result.thumbnail=movie.thumbnail
    if movie.description!=None:
       result.description=movie.description
    if movie.genre!=None:
       result.genre=movie.genre
       
    await result.save()
    return result

@movies_router.delete('/{movie_id}')
async def deletemovie(movie_id:PydanticObjectId):
    result=await Movie.get(movie_id)
    await result.delete()
    return {'message':'The movie is deleted successfully'}