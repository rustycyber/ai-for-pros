from flask import Flask, jsonify
app = Flask(__name__)

# Sample User Data Model
users_db = {1: {"name": "Alice", "role": "Engineer"}}

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Intentional Bug: Unhandled key error causes a 500 status code
    user = users_db[user_id] 
    return jsonify({"status": "success", "data": user}), 200

if __name__ == '__main__':
    app.run(port=5000)
