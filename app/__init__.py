from flask import Flask
from flask_restful import Api
from .resources import UserView, UserListView
from .config import  connect_database

def create_app():
    app = Flask(__name__)    
    connect_database(app)
    
    api = Api(app)
    api.add_resource(UserListView, '/users')
    api.add_resource(UserView, '/users/<string:user_id>')

    return app
