
# -*- coding: utf-8 -*-
# № 16/5. Завершаем первую версию crud # Запуск в main

from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []  # данные все запишим в users


class User(BaseModel):  # содержит в себе
    id: int = None   # номер пользователя
    username: str       # имя пользователя
    age: int            # возраст пользователя


@app.get("/users")  # если мы получили .get("/")-гет запрос
def Get_All_Users() -> List[User]:  # возвращает список сообщений
    return users


@app.get(path="/user/{user_id}")  # если мы получили .get("/")-гет запрос
def Get_User(user_id: int) -> User:  # то отработай эту функцию
    try:
        return users[user_id]  # возвращает конкретное сообщение которое у нас есть
    except ImportError:
        raise HTTPException(status_code=404, detail="User not found")  # или ловим ошибку


@app.post("/user/{username}/{age}")
def Create_User(username: str, age: int) -> User:
    user_id = len(users) + 1  # Определяем id для нового пользователя

    new_user = User(id=user_id, username=username, age=age)  # Создаем нового пользователя

    users.append(new_user)  # Добавляем пользователя в список

    return new_user  # Возвращаем созданного пользователя


@app.put("/user/{user_id}/{username}/{age}")  # если мы получили .get("/")-гет запрос
def Update_User(user_id: int, age: int, username: str = Body) -> str:  # то отработай эту функцию
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return f"User updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")  # или ловим ошибку


@app.delete("/user/{user_id}")  # если мы получили .get("/")-гет запрос, т.е.удаление сообщения
def Delete_User(user_id: int) -> str:  # то отработай эту функцию
    try:
        users.pop(user_id)
        return f"User ID={user_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User Was not found")  # или ловим ошибку


@app.delete("/")  # если мы получили .get("/")-гет запрос, т.е.удаление сообщения
def Kill_User_All() -> str:  # то отработай эту функцию
    users.clear()
    return "All User deleted!"


