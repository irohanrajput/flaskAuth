from flask_restful import Resource, reqparse, fields, marshal_with
from .models import User
from .utils import hash_password

user_parser = reqparse.RequestParser()
user_parser.add_argument("name", type=str, required=True, help="Name cannot be blank")
user_parser.add_argument("email", type=str, required=True, help="Email cannot be blank")
user_parser.add_argument(
    "password", type=str, required=True, help="Password cannot be blank"
)

user_fields = {
    "id": fields.String(attribute=lambda x: str(x.id)),
    "name": fields.String,
    "email": fields.String,
}


class UserListView(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = User.objects()
        return list(users), 200

    @marshal_with(user_fields)
    def post(self):
        args = user_parser.parse_args()
        hashed_password = hash_password(args["password"])
        user = User(name=args["name"], email=args["email"], password=hashed_password)
        user.save()
        return user, 201


class UserView(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        user = User.objects(id=user_id).first()
        if user:
            return user, 200
        return {"error": "User not found"}, 404

    @marshal_with(user_fields)
    def put(self, user_id):
        args = user_parser.parse_args()
        user = User.objects(id=user_id).first()
        if user:
            user.name = args["name"]
            user.email = args["email"]
            if args["password"]:
                user.password = hash_password(args["password"])
            user.save()
            return user, 200
        return {"error": "User not found"}, 404

    def delete(self, user_id):
        user = User.objects(id=user_id).first()
        if user:
            user.delete()
            return "", 204
        return {"error": "User not found"}, 404
