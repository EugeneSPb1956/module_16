# -*- coding: utf-8 -*-

from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
def post_user(username: str, age: int) -> str:
    user_keys = [int(i) for i in users.keys()]
    user_id = max(user_keys) + 1
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int, username: str, age: int) -> str:
    try:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f'User {user_id} is updated'
    except IndexError:
        raise HTTPException(status_code=404, detail=f'User {user_id} not found')


@app.delete('/user/{user_id}')
def delete_user(user_id: str) -> str:
    print(user_id, type(user_id))
    try:
        users.pop(user_id)
        return f'User {user_id} has been deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail=f'User {user_id} not found')

# ...$ python3 -m uvicorn module_16_3:app
