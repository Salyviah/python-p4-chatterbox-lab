# server/testing/app_test.py

import pytest
from app import app, db, Message

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the tables
        yield client
        with app.app_context():
            db.drop_all()  # Drop the tables after tests

class TestApp:
    def test_get_message_empty(self, client):
        response = client.get('/message')
        assert response.status_code == 200
        assert response.json == []  # Expecting an empty list if no messages are present

    def test_create_and_get_message(self, client):
        # Create an instance of Message
        new_message = Message(body="Hello 👋")
        with app.app_context():
            db.session.add(new_message)
            db.session.commit()

        response = client.get('/message')
        assert response.status_code == 200
        assert len(response.json) == 1
        assert response.json[0]['body'] == "Hello 👋"
