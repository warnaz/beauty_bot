from pymongo import MongoClient
from datetime import datetime


# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Добавление документа с полем createdAt
document = {
    "data": "example data",
    "createdAt": datetime.utcnow()  # Текущая дата и время по UTC
}
collection.insert_one(document)

# Создание TTL индекса на поле createdAt с временем жизни 24 часа (86400 секунд)
collection.create_index("createdAt", expireAfterSeconds=86400)
