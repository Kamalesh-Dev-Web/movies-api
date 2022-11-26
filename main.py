from typing import Union

from fastapi import FastAPI

from movies import movies_router
from database import init_db
from mangum import Mangum

app = FastAPI()
handler=Mangum(app)

app.include_router(movies_router,prefix='/movies')

@app.on_event('startup')
async def connect():
    await init_db()
    
    