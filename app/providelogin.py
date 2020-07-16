import os
import requests
from flask import redirect, url_for, render_template
from flask_login import current_user, login_user, LoginManager
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.forms.loginForm import LoginForm
from app.models.user import lfUser

class lfForeningletLogin():
    apiPass = os.environ.get('API_PASSWORD')
    apiUser = os.environ.get('API_USERNAME')
    url = 'https://foreninglet.dk/api/memberlogin?version=1'
    login_manager = LoginManager()
    loggedInUser = lfUser()

    current_user
    def __init__(self, app):
        self.login_manager.init_app(app)

    def login(self):
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()
        if form.validate_on_submit():
            pass
            #login_user(user)
        return render_template('login.html', title='Sign In', form=form)
    
    def login_user(self,username, password):
        data = {
            "credentials": {
                "email": username,
                "password": password,
                "field": "email"

            }
        }
        try:
            r = requests.post(self.url, auth=(self.apiUser,self.apiPass),json=data, headers={'Content-Type': 'application/json'})
            userData = r.json()
            
        except requests.exceptions.RequestException:
            return None

    
    @login_manager.user_loader
    def load_user(self, user_id):
        return self.loggedInUser.get(user_id)


