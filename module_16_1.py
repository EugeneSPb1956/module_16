# -*- coding: utf-8 -*-

from fastapi import FastAPI, Path
from typing import Annotated

# -- 1
app = FastAPI()

# -- 4
@app.get('/user/admin')
async def admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}

# -- 3
@app.get('/user/{user_id}')
async def user_id_page(user_id: Annotated[int, Path(de=0, le=100, description='Введите ваш id пользователя', example='123')]) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

# -- 5
@app.get('/user/{username}/{age}')
# async def user_page(user_id: Annotated[int, Path(de=0, le=100, description='Введите ваш id пользователя', example='123')]) -> dict:
async def user(username: Annotated[
    str, Path(min_length=3, max_length=15, description='Введите ваше имя и возраст', example='Евгений, 24')]
                   , age: int) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

# -- 2
@app.get('/')
async def main_page() -> dict:
    return {'message': 'Главная страница'}

