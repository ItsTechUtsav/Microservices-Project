from fastapi import FastAPI

app = FastAPI()

# dummy database
users = []

@app.get("/")
def home():
    return {"message": "User Service Running"}

@app.post("/add-user")
def add_user(name: str):
    user = {"id": len(users) + 1, "name": name}
    users.append(user)
    return {"message": "User added", "user": user}

@app.get("/users")
def get_users():
    return users

import requests

@app.get("/products-from-product-service")
def get_products():
    response = requests.get("http://product-service:8002/products")
    return response.json()