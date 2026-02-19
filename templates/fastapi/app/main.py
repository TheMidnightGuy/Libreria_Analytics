#Obtenemos resultados en http://127.0.0.1:8000/docs

from fastapi import Depends, FastAPI # type: ignore

from .dependencies import get_query_token, get_token_header
from .internal import admin #importamos las funciones de admin en la carpeta internal
from .routers import items, users #importamos las funciones de los archivos en la carpeta /routers

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}