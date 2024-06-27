        # Архитектура

# 1. Веб-сервер
        # - Фреймворк или вебсервер(например, Flask, Fastapi, Django)
# 2. Endpoint Обработки Веб-Хуков
        # - /Datalore, который принимает POST запросы от веб-хуков
# 3. Разбор Тела Запроса
        # - JSON, который приходит в тело запроса
# 4. Роутинг и Вызов Функций
        # - Функция, которая обрабатывает запрос
        # - Роутинг, чтобы определить, какую функцию обрабатывать


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


# Создаем модель Pydantic для ожидаемых данных запроса
class WebhookData(BaseModel):
    function: str
    data: Optional[dict] = None


# Словарь функций для обработки
functions = {
    "functionA": lambda data: {"result": "A processed"},
    "functionB": lambda data: {"result": "B processed"},
}


@app.post('/Datalore')
def handle_webhook(webhook_data: WebhookData):
    function_name = webhook_data.function
    data = webhook_data.data

    # Проверяем, существует ли функция
    if function_name in functions:
        # Вызываем функцию и возвращаем результат
        return functions[function_name](data)
    else:
        # Если функция не найдена, отправляем ошибку 404
        raise HTTPException(status_code=404, detail="Function not found")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)