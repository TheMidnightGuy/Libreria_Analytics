#Fastapi dev app/routers/models.py
#Obtenemos resultados en http://127.0.0.1:8000/models/names
#modelos disponibles: alexnet, lenet, resnet

from enum import Enum

from fastapi import FastAPI #type: ignore


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

@app.get("/models/names")
async def read_models_names():
    return{"Models names available: alexnet, resnet, lenet"}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}