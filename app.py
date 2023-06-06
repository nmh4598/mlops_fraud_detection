import time
import asyncio

from pydantic import BaseModel, validator
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"we expect price >= 0, we received {value}")
        return value


@app.get("/")
def root():
    return {"message": "hello world again"}


@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}


@app.post("/items/")
def create_item(item: Item):
    return item


@app.get("/sleep_slow")
def sleep_slow():
    _ = time.sleep(1)
    return {"status": "done"}


@app.get("/sleep_fast")
async def sleep_fast():
    _ = await asyncio.sleep(1)
    return {"status": "done"}
