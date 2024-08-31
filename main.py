from http.client import HTTPException
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

users = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/users/{user_id}")
def create_user(user_id: int, name: str):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User already exists")

    users[user_id] = {"name": name}
    return {"user_id": user_id, "name": name}


@app.get("/user/{user_id")
def read_user(user_id: int):
    user = users.get(user_id)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return user

@app.put("/user/{user_id}")
def update_user(user_id: int, name: str):
    if user_id not in users:
        raise HTTPException(status_code=400, detail="User not found")
    users[user_id] = {"name": name}
    return {"user_id": user_id, "name": name}

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=400, detail="User not found")
    del users[user_id]
    return {"detail": "User deleted"}


