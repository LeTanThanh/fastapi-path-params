from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
  return { "item_id": item_id }

@app.get("/users/me")
async def read_me():
  return { "user_id": "The current user" }

@app.get("/users/{user_id}")
async def read_user(user_id: int):
  return { "user_id": user_id }

@app.get("/users")
async def read_users():
  return ["Rick", "Morty"]

class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"

@app.get("/models/{model_name}")
async def read_model_name(model_name: ModelName):
  match model_name:
    case ModelName.alexnet:
      message = "Deep Learning FTW!"
    case ModelName.resnet:
      message = "LeCNN all the images"
    case ModelName.lenet:
      message = "Have some residuals"

  return {"model_name": model_name, message: message}

"""
Path convertor

Using an option directly from Starlette you can declare a path parameter containing a path using a URL like:

/files/{file_path:path}

In this case, the name of the parameter is file_path, and the last part, :path, tells it that the parameter should match any path.

So, you can use it with:
"""
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
  return {"file_path": file_path}
