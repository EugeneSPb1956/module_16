# -*- coding: utf-8 -*-

from fastapi import FastAPI

# -- 1
app = FastAPI()


# -- 2
@app.get('/')
async def main_page() -> dict:
    return {'message': 'Главная страница'}


# -- 4
@app.get('/user/admin')
async def admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}


# -- 3
@app.get('/user/{user_id}')
async def user_id_page(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


# -- 5
@app.get('/user')
async def user(username: str = 'alex', age: int = 24) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
