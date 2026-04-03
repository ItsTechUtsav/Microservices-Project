from fastapi import FastAPI

app = FastAPI()

products = []

@app.get("/")
def home():
    return {"message": "Product Service Running Successfully"}

@app.post("/add-product")
def add_product(name: str):
    product = {"id": len(products) + 1, "name": name}
    products.append(product)
    return {"message": "Product added", "product": product}

@app.get("/products")
def get_products():
    return products