from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

import uvicorn

app = FastAPI()

class SampleRequest(BaseModel):
    a: int
    b: int


@app.post("/add")
def add(this_request: SampleRequest):
    return {"result": (this_request.a + this_request.b)}


@app.post("/mul")
def mul(this_request: SampleRequest):
    return {"result": (this_request.a * this_request.b)}
