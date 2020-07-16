import os
from app.providelogin import lfForeningletLogin
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.config.from_envvar('APP_ENVVARFILE')

# Session handling for Login
from flask import session, redirect, url_for, request
from markupsafe import escape

from flask_login import LoginManager, login_required, logout_user, login_user, current_user
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = os.environ.get('FLASK_LOGIN_SECRET')

# Move this somewhere else
import requests

import json
@app.route('/')

def hello_world():
    apiPass = os.environ.get('API_PASSWORD')
    apiUser = os.environ.get('API_USERNAME')
    envVar = os.environ.get('TESTVAR')
    response = _loginToForeningLet(apiUser, apiPass)
    apiAuthenticated = False
    if response.status_code == 200:
        apiAuthenticated = True
        jsonResponse = _getActivities(apiUser, apiPass)
        activities = _makeActivityTable(jsonResponse.text)
    return render_template('index.html', activities=activities, unionId='3196')
    #return 'Hello World! {} - {} - {} <br> {}'.format(response.status_code, apiAuthenticated, envVar, activities)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     session ['username'] = request.form['username']
    #     return redirect(url_for('index'))
    # return '''
    #     <form method="post">
    #     <p><input type=text name=username>
    #     <p><input type=submit value=Login>
    # '''
    fll = lfForeningletLogin(app)
    return fll.login()

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

def _loginToForeningLet(apiUser,apiPass):
    url = 'https://foreninglet.dk/api/activities?version=1'
    try:
        r = requests.get(url, auth=(apiUser,apiPass))
        return r
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def _getActivities(apiUser,apiPass):
    url = 'https://foreninglet.dk/api/activities?version=1'
    try:
        r = requests.get(url, auth=(apiUser,apiPass))
        return r
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def _makeActivityTable(jsonObject):
    activities = ''
    price = dict()
    activity_json = json.loads(jsonObject)
    outActivities = list()
    for activity in activity_json:
        if activity['Name'] in ('Indmeldelse'):
            for specifics in activity['ExternalDescriptions']:
                if specifics['Headline'] == 'Pris':
                    price = specifics['Text']
            activities += "{}: {}<br>".format(activity['Name'], price)
            actDict = {
                    'name': activity['Name'],
                    'price': price,
                    'id': activity['ActivityId']
                }
            outActivities.append(actDict)
    
    return outActivities
