from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configure MongoDB
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

# Explicitly use "myDatabase" as the database name
db = mongo.cx["myDatabase"]  # Use mongo.cx (client) to specify DB name
users_collection = db["myCollection"]    # Define the "users" collection

# Ensure database and collection exist
if users_collection.count_documents({}) == 0:
    users_collection.insert_one({"name": "Test User"})

@app.route('/')
def home():
    return "Welcome to Flask with MongoDB Atlas!"

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    user_id = users_collection.insert_one({"name": data["name"]}).inserted_id
    return jsonify({"message": "User added", "id": str(user_id)})

@app.route('/get_users', methods=['GET'])
def get_users():
    users = list(users_collection.find({}, {"_id": 0, "name": 1}))
    return jsonify(users)

# Debugging route to check available endpoints
@app.route('/routes', methods=['GET'])
def list_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])

# Fixed this line!
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
