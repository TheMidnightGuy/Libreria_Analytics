#Podemos probar la funcion de tokens dentro de http://127.0.0.1:8000/docs

#items > GET /items/ Read items
#Ingresamos los siguentes token simulados
#token:  token-query
#x-token:  token-header
#deberiamos obtener un output detallado del item.

#

from typing import Annotated

from fastapi import Header, HTTPException #type: ignore


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "token-header":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "token-query":
        raise HTTPException(status_code=400, detail="No Jessica token provided")