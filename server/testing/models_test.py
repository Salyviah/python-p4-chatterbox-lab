# server/testing/models_test.py

from models import db, Message

class TestMessage:
    def test_message_creation(self):
        # Create an instance of Message
        message = Message(body="Hello 👋")
        assert message.body == "Hello 👋"

    def test_message_serialization(self):
        # Create an instance of Message
        message = Message(body="Hello 👋")
        serialized = message.to_dict()  # Using SerializerMixin
        assert serialized['body'] == "Hello 👋"
