# 🔗 Shortly — сервис сокращения ссылок

Простой и быстрый API для сокращения длинных ссылок.  
Ты отправляешь URL — получаешь короткий код. Переходишь по коду — попадаешь на оригинал.

---

## 🚀 Стек

- **Python**
- **FastAPI**
- **PostgreSQL**
- **Alembic**
- **Pydantic**
- **SQLAlchemy**

---

## 🛠 Установка и запуск

```bash
# Клонируем
git clone https://github.com/Lalka12235/shortly.git
cd shortly

# Устанавливаем зависимости
pip install -r requirements.txt

# Запускаем сервер
uvicorn main:app --reload
