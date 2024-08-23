# crud.py
from typing import List, Optional
from models import User

# Simulated in-memory storage
users_db = []
current_id = 1

def add_user(user: User) -> User:
    global current_id
    user.id = current_id
    current_id += 1
    users_db.append(user)
    return user

def get_users(page: int, limit: int) -> List[User]:
    start = (page - 1) * limit
    end = start + limit
    return users_db[start:end]

def search_users(keyword: str) -> List[User]:
    return [user for user in users_db if keyword.lower() in user.name.lower()]

def update_user(user_id: int, user_data: User) -> Optional[User]:
    for user in users_db:
        if user.id == user_id:
            user.name = user_data.name
            user.email = user_data.email
            user.age = user_data.age
            return user
    return None

def delete_user(user_id: int) -> bool:
    global users_db
    users_db = [user for user in users_db if user.id != user_id]
    return True
