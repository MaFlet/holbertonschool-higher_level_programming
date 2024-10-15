from flask import Flask
from flask import request
from flask import jsonify
from flask import abort


app = Flask(__name__)
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return jsonify({"status": "OK"})

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        abort(404)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if not data or 'username' not in data or 'name' not in data:
        abort(400, description="Invalid input: 'username' and 'name' are required")

    username = data['username']
    if username in users:
        abort(400, description="User already exists")
    
    users[username] = {
        "name": data['name'],
        "age": data.get('age', 0),
        "city": data.get('city', "Unknown")
    }

    return jsonify({"message": "User added succesfully!", "user": users[username]}), 201

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "404 Not Found", "message": "Endpoint not found."}), 404

if __name__ == "__main__": 
    app.run(host = "localhost", port = 8000)
