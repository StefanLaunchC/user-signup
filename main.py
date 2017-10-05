from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup.html')

def is_username():
    if {username} 



@app.route('/', methods=['POST'])
def user_signup():

    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    usernam_error = ''
    password_error = ''
    verifypassword_error = ''
    email_error = ''

    if not is_ok(username):

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return '<h1>Welcome {username}!</h1>'



app.run()