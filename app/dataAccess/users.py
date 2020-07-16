from app.models.user import User
import os

class UserDAO:

    def __init__(self):
        apiPass = os.environ.get('API_PASSWORD')
        apiUser = os.environ.get('API_USERNAME')
        url = 'https://foreninglet.dk/api/memberlogin?version=1'
    

    def get(self, user_id):
        if user_id in self.valid_users:
            user = User(user_id)
            return user
        else:
            return None

    def validate(self, user_id):
        return user_id in self.valid_users