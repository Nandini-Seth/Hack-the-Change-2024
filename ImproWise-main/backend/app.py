import os
import openai
import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for session handling
CORS(app)

# Initialize SQLite database
def init_db():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE
            )
        ''')
        conn.commit()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Call init_db to ensure database is initialized when the app starts
init_db()

@app.route('/api/chatbot', methods=['POST'])
def chatbot_response():
    data = request.json
    user_question = data.get("question", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_question}
            ]
        )
        answer = response.choices[0].message['content'].strip()
        return jsonify({"answer": answer})
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return jsonify({"error": str(e)}), 500

# Route to save email data to the database, ignoring duplicates
@app.route('/api/save_email', methods=['POST'])
def save_email():
    data = request.json
    email = data.get('email', '')  # Default to an empty string if 'email' is not provided
    
    try:
        # Insert email into the database, ignoring duplicates
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO users (email) VALUES (?)", (email,))
        conn.commit()
        conn.close()

        # Confirm success
        print("Email saved to database:", email)
        return jsonify({"message": "Email saved successfully!"}), 200
    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({"error": "Failed to save email."}), 500

if __name__ == '__main__':
    app.run(debug=True)
