from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

import uvicorn
import os

app = FastAPI()

class SampleRequest(BaseModel):
    a: int
    b: int


# dir_path = '/opt/act/dc/'
auc_ais_settings_file = os.getenv('AUC_AIS_SETTINGS_FILE')


@app.post("/add")
def add(this_request: SampleRequest):
    import os

    filename = auc_ais_settings_file

    if os.path.exists(filename):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not

    f = open(filename, append_write)
    f.write("add : " + str(this_request.a + this_request.b) + '\n')
    f.close()
    return {"result": (this_request.a + this_request.b)}


@app.post("/mul")
def mul(this_request: SampleRequest):
    import os

    filename = auc_ais_settings_file

    if os.path.exists(filename):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not

    f = open(filename, append_write)
    f.write("mul : " + str(this_request.a * this_request.b) + '\n')
    f.close()
    return {"result": (this_request.a * this_request.b)}
