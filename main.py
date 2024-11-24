from fastapi import FastAPI
from routers import category, products
import asyncio
import uvicorn


app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "My shop"}

app.include_router(category.router)


if __name__ == "__main__":
    asyncio.run(uvicorn.run(app, host="127.0.0.1", port=8000, loop="asyncio"))