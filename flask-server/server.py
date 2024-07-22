from flask import Flask, request
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from uuid import uuid4

app = Flask(__name__)
CORS(app, supports_credentials=True, methods=['GET', 'POST', 'OPTIONS'], allow_headers=['Content-Type', 'Authorization'])
client = MongoClient("mongodb://localhost:27017/")
db = client["clients"]
collection = db["user"]

try:
    client.admin.command('ismaster')
    print("Connected to the MongoDB database.")
except Exception as e:
    print("Failed to connect to the MongoDB database:", str(e))
rand_token = uuid4();

@app.route('/signup', methods=['GET', 'POST'])
def signUp():
    bodyRequest = request.get_json();
    bodyRequest['auth_token'] = str(uuid4())
    data = collection.insert_one(bodyRequest).inserted_id
    print('Response Data:', data)
    return jsonify({"status": "success", "data": str(data)})

@app.route('/login', methods=['GET', 'POST'])
def signIn():
    bodyRequest = request.get_json();
    bodyRequest['auth_token'] = str(uuid4())
    data = collection.insert_one(bodyRequest)
    insert = data.inserted_id
    print('Response Data:', data)
    return jsonify({"status": "success", "data": str(data)})

if __name__ == '__main__':
    app.run(debug=True)
