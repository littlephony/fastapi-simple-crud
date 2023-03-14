from fastapi import FastAPI
from .router import router

app = FastAPI()

@app.get("/")
async def hello() -> dict:
    return { "message": "Hello, World!"}

app.include_router(router)
