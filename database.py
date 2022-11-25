import motor
import motor.motor_asyncio
from models import Movie
from beanie import init_beanie


async def init_db():
    client=motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://kamalesh-mongo:Vwxps38mE@cluster0.h5lf0.mongodb.net/?retryWrites=true&w=majority")
    await init_beanie(database=client.db_name, document_models=[Movie])