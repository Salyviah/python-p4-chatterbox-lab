# server/app.py

from flask import Flask, jsonify
from flask_cors import CORS
from models import db, Message

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Update with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Example route
@app.route('/message', methods=['GET'])
def get_message():
    # Retrieve all messages from the database
    messages = Message.query.all()
    return jsonify([message.to_dict() for message in messages])  # Using SerializerMixin for dict conversion

if __name__ == '__main__':
    app.run(debug=True)
