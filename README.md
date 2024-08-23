FastAPI CRUD Operations
This project is a FastAPI application that provides CRUD (Create, Read, Update, Delete) operations for user data using MongoDB as the database. The application includes basic functionalities to manage user information.

Project Structure
model.py: Contains the MongoDB document model.
main.py: The main FastAPI application with endpoints for user operations.
crud.py: Contains helper functions for database operations.
database.py: Manages the MongoDB connection and provides the users_collection for CRUD operations.

Setup Instructions
1. Clone the Repository
git clone https://github.com/Vaishnavipawar0901/Fastapi-.git
cd Fastapi-

2. Activate Virtual Environment
.\venv\Scripts\activate  # For Windows
source venv/bin/activate  # For macOS/Linux

3.Run the Application
uvicorn main:app --reload
(The application will be running at http://127.0.0.1:8000.)


Endpoints
POST /users: Create a new user.
GET /users: Retrieve a list of users with pagination.
GET /users/{user_id}: Retrieve a user by ID.
PUT /users/{user_id}: Update a user by ID.
DELETE /users/{user_id}: Delete a user by ID.


Notes
Replace the MongoDB connection string in database.py with your own MongoDB URL.
Ensure MongoDB is running and accessible from your application.
