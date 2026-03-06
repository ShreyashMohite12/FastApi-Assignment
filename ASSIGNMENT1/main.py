from fastapi import FastAPI

app = FastAPI()

# Products list
products = [
    {"id": 1, "name": "Notebook", "price": 50, "category": "Stationery", "in_stock": True},
    {"id": 2, "name": "Pen", "price": 10, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Headphones", "price": 1500, "category": "Electronics", "in_stock": True},
    {"id": 4, "name": "Mouse", "price": 700, "category": "Electronics", "in_stock": False},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False}
]

@app.get("/")
def home():
    return {"message": "FastAPI Store API"}

@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }
@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    
    result = [p for p in products if p["category"] == category_name]

    if not result:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }
@app.get("/products/instock")
def get_instock():

    available = [p for p in products if p["in_stock"] == True]

    return {
        "in_stock_products": available,
        "count": len(available)
    }
@app.get("/store/info")
def store_info():

    return {
        "store_name": "Tech Store",
        "total_products": len(products),
        "categories": list(set([p["category"] for p in products]))
    }
@app.get("/products/search/{name}")
def search_product(name: str):

    result = [p for p in products if name.lower() in p["name"].lower()]

    if not result:
        return {"message": "Product not found"}

    return {
        "search": name,
        "results": result
    }
@app.get("/products/price-stats")
def price_stats():

    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "cheapest_product": cheapest,
        "most_expensive_product": expensive
    }