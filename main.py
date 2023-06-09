from enum import Enum
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/items0/{item_id}")
async def read_item(item_id:int):
    return {"item_id":item_id}



@app.get("/users/me")
async def read_user_me():
    return {"user_id":"the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id:str):
    return {"user_id": user_id}


class ModelName(str, Enum):
    alexnet ="alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/modles{model_name}")
async def get_model(model_name :ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name,"message":"Deep Learning FTW!"}
    if model_name == ModelName.alexnet:
        return {"model_name":model_name,"message":"LeCNN all the images!"}
    
    return {"model_name":model_name,"message":"Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
    

# 查询参数

fake_items_db = [{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0 , limit: int=0):
    return fake_items_db[skip : skip + limit]
