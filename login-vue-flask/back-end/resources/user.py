from flask_restful import Resource, reqparse

from models.user import User


parser = reqparse.RequestParser()


class UserEndPoint(Resource):
    def post(self):
        parser.add_argument(
            "username",
            help="username can not be none",
            required=True
        )
        parser.add_argument(
            "password",
            help="password can not be none",
            required=True
        )

        post_data = parser.parse_args()
        print(post_data)

        user = User(
            username=post_data["username"],
            password=post_data["password"]
        )
        try:
            user.save()

            return {"message": "Register success"}
        except Exception as e:
            print(e)
            return {"message": "Some thing went wrong"}
