#Modificar comentarios según cambios y ejecución.!!!

#Fastapi dev app/routers/users.py
#Obtenemos resultados en http://127.0.0.1:8000/users/me

from fastapi import APIRouter #type: ignore

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}