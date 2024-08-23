from pymongo import MongoClient

# Replace with your MongoDB connection string
MONGO_DB_URL = "mongodb+srv://badvibess1777:KOMNUEeDplk4fetG@cluster0917.wmx48.mongodb.net/"

client = MongoClient(MONGO_DB_URL)
db = client["Database"]

users_collection = db["users"]
