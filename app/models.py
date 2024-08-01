from mongoengine import Document, StringField, EmailField

class User(Document):
    name = StringField(required=True, max_length=50)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
