from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/add")
def add(a: int, b: int):
    return {"result": (a + b)}


@app.get("/mul")
def mul(a: int, b: int):
    return {"result": (a * b)}
