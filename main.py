from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from bson import ObjectId
from database import users_collection  # Import the users collection from database.py

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

# Helper function to convert MongoDB documents to JSON serializable format
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
    }

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI User Management API!"}

@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    new_user = user.dict()
    result = users_collection.insert_one(new_user)
    created_user = users_collection.find_one({"_id": result.inserted_id})
    return user_helper(created_user)

@app.get("/users")
async def get_users(page: int = 1, limit: int = 10):
    users = users_collection.find().skip((page - 1) * limit).limit(limit)
    return [user_helper(user) for user in users]

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_helper(user)
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}")
async def update_user(user_id: str, user: User):
    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user.dict()}
    )
    if result.modified_count:
        updated_user = users_collection.find_one({"_id": ObjectId(user_id)})
        return user_helper(updated_user)
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count:
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")