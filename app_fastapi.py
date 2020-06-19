from fastapi import FastAPI
from sync_db import get_row


app = FastAPI()

@app.get("/test")
def test():
    a, b = get_row()
    return {"a": str(a).zfill(10), "b": b}
