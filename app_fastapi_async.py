from fastapi import FastAPI
from async_db import get_row


app = FastAPI()

@app.get("/test")
async def test():
    a, b = await get_row()
    return {"a": str(a).zfill(10), "b": b}
