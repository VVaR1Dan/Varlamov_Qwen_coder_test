from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import sqlite3

app = FastAPI(title="Marketplace Product API")

# CORS для фронтенда на localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "products.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            color TEXT,
            size TEXT,
            material TEXT,
            description TEXT
        )
    ''')
    
    # Проверка, есть ли уже данные
    cursor.execute('SELECT COUNT(*) FROM products')
    count = cursor.fetchone()[0]
    
    if count == 0:
        # Добавляем демо-данные
        demo_products = [
            ('Футболка хлопковая', 1500.0, 'Белый', 'M', 'Хлопок', 'Классическая белая футболка из 100% хлопка. Подходит для повседневной носки.'),
            ('Стул офисный', 8500.0, 'Черный', 'Универсальный', 'Металл, пластик', 'Эргономичный офисный стул с регулируемой высотой и подлокотниками.')
        ]
        cursor.executemany('''
            INSERT INTO products (name, price, color, size, material, description)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', demo_products)
        conn.commit()
    
    conn.close()

# Pydantic модели
class ProductBase(BaseModel):
    name: str
    price: float
    color: Optional[str] = None
    size: Optional[str] = None
    material: Optional[str] = None
    description: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    
    class Config:
        from_attributes = True

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/products", response_model=List[ProductResponse])
async def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    conn.close()
    
    products = []
    for row in rows:
        products.append({
            "id": row["id"],
            "name": row["name"],
            "price": row["price"],
            "color": row["color"],
            "size": row["size"],
            "material": row["material"],
            "description": row["description"]
        })
    return products

@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return {
        "id": row["id"],
        "name": row["name"],
        "price": row["price"],
        "color": row["color"],
        "size": row["size"],
        "material": row["material"],
        "description": row["description"]
    }

@app.post("/products", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, price, color, size, material, description)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (product.name, product.price, product.color, product.size, product.material, product.description))
    conn.commit()
    product_id = cursor.lastrowid
    conn.close()
    
    return {
        "id": product_id,
        "name": product.name,
        "price": product.price,
        "color": product.color,
        "size": product.size,
        "material": product.material,
        "description": product.description
    }

@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product: ProductUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Проверка существования товара
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    row = cursor.fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")
    
    cursor.execute('''
        UPDATE products
        SET name = ?, price = ?, color = ?, size = ?, material = ?, description = ?
        WHERE id = ?
    ''', (product.name, product.price, product.color, product.size, product.material, product.description, product_id))
    conn.commit()
    conn.close()
    
    return {
        "id": product_id,
        "name": product.name,
        "price": product.price,
        "color": product.color,
        "size": product.size,
        "material": product.material,
        "description": product.description
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
