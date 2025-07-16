import uvicorn
from fastapi import FastAPI,Body
from pydantic import EmailStr,BaseModel
app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_world():
    return {
        "message": "Hello World!"
    }
@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello, {name}!"}

@app.post("/users/")
def crete_user(user: CreateUser):
    return {
        "message" : "Success!",
        "email" : user.email,
    }

@app.post("/calc/add/")
def add(a: int , b : int ):
    return {
        "a" : a,
        "b" : b,
        "result" : a + b,
    }
@app.get("/items/")
def list_items():
    return[
        "item1",
        "item1"]

@app.get("/items/latest/")
def get_latest():
    return {
        "item1": {
            "id": 1,
            "name": "latest",
        },
    }


@app.get("/items/{item_id}/")
def get_item(item_id: int):
    return {
        "item":{
            "id" : item_id,
        },
    }

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)