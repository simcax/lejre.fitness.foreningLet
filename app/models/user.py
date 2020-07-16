from flask_login import UserMixin
import json

class lfUser(UserMixin):

    def __init__(self):
        self.id = ""
        self.display_id = ""
        self.first_name = ""
        self.last_name = ""
        self.address = ""
        self.address2 = ""
        self.zip = ""
        self.city = ""
        self.email = ""
        self.birthday = ""
        self.enrollment = ""
        self.last_login = ""
        self.password = ""
        
    def get_id(self, lf_user_json_obj):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    