#Fastapi dev app/main.py

#Podemos probar la funcion de tokens dentro de http://127.0.0.1:8000/docs
#items > GET /items/ Read items
#Ingresamos los siguentes token simulados
#token:  token-query
#x-token:  token-header
#deberiamos obtener un output detallado del item.



from fastapi import APIRouter, Depends, HTTPException # type: ignore
from ..dependencies import get_token_header


router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description":"Notfound"}},
)

#Para la busqueda de items en API docs. usamos de item id: Agua, Cereal

items_from_db = {"Agua": {"name": "Agua Mineral"}, "Cereal": {"name":"Cereal"}}

@router.get("/items")
async def read_items():
    return items_from_db

@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in items_from_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": items_from_db[item_id]["name"], "item_id": item_id}

#Agregamos tags, dependencias y responses
@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}