from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('rule_engine.db')
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json['data']
    age = data['age']
    department = data['department']
    salary = data['salary']
    experience = data['experience']

    # Example logic to determine eligibility based on rules
    is_eligible = False

    # Check if the user matches the rules
    if (age > 30 and department == 'Sales') or (age < 25 and department == 'Marketing'):
        is_eligible = True
    elif (salary > 50000 or experience > 5):
        is_eligible = True
    elif (age > 30 and department == 'Marketing'):
        is_eligible = True
    elif (salary > 20000 or experience > 5):
        is_eligible = True

    return jsonify({"result": is_eligible})

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])  # Convert rows to a list of dictionaries

if __name__ == '__main__':
    app.run(debug=True)
