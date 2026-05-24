# Marketplace Product App

Веб-приложение для заполнения и редактирования карточек товаров на маркетплейсе.

## Структура проекта

```
marketplace-app/
├── backend/
│   ├── main.py           # FastAPI сервер
│   └── requirements.txt  # Python зависимости
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── main.js
        ├── App.vue
        ├── assets/
        │   └── main.css
        ├── router/
        │   └── index.js
        └── views/
            ├── ProductList.vue
            ├── ProductEdit.vue
            └── ProductCreate.vue
```

## Установка и запуск

### 1. Backend (Python + FastAPI)

```bash
cd marketplace-app/backend

# Создание виртуального окружения (опционально, но рекомендуется)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

# Установка зависимостей
pip install -r requirements.txt

# Запуск сервера
python main.py
# или
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend будет доступен по адресу: **http://localhost:8000**

API endpoints:
- `GET /products` — получить все товары
- `GET /products/{id}` — получить один товар
- `POST /products` — создать товар
- `PUT /products/{id}` — обновить товар

Документация API автоматически доступна по адресу: **http://localhost:8000/docs**

### 2. Frontend (Vue 3 + Vite)

Откройте новый терминал:

```bash
cd marketplace-app/frontend

# Установка зависимостей
npm install

# Запуск в режиме разработки
npm run dev
```

Frontend будет доступен по адресу: **http://localhost:5173**

## Функционал

1. **Главная страница** (`/`) — список всех товаров с названием, ценой и ID
2. **Карточка товара** (`/product/:id`) — редактирование всех полей товара
3. **Создание товара** (`/create`) — форма для добавления нового товара

## Демо-данные

При первом запуске backend автоматически создаёт таблицу и добавляет два товара:
- Футболка хлопковая (1500 ₽)
- Стул офисный (8500 ₽)

## Технологии

- **Backend**: FastAPI, SQLite, Pydantic
- **Frontend**: Vue 3 (Composition API), Vue Router, Axios, Vite
- **Стили**: CSS (без фреймворков)
