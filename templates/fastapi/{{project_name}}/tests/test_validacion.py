##Se validan las funciones de FastAPI con PyTest
#Funciones validadas 
# endpoints basicos (GET)
# endpoints con query params
# endpoints con response model
# status codes

from fastapi.testclient import TestClient #type: ignore
from app.main import app

client = TestClient(app)

root_fake_token = "/?token=token-query"
user_fake_token = "/users/?token=token-query"
item_fake_token = "/items/?token=token-query"

def test_read_root():
    response = client.get(root_fake_token)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Bigger Applications!"}

def test_read_users():
    response = client.get(user_fake_token)
    assert response.status_code == 200
    assert response.json() == [{"username":"Rick"},{"username":"Morty"}]

