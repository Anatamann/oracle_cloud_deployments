from flask import Flask, jsonify, send_from_directory
import sqlite3
import random

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/get-message')
def get_message():
    conn = sqlite3.connect('messages.db')
    cur = conn.cursor()
    cur.execute("SELECT text FROM messages")
    messages = cur.fetchall()
    conn.close()
    random_message = random.choice(messages)[0]
    return jsonify({'message': random_message})

if __name__ == '__main__':
    app.run(debug=True)