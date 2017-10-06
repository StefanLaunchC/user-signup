from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('inputs.html')


@app.route("/", methods=['POST'])
def form_info():

    email = request.form["email"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    username = request.form["username"]

    email_err = ''
    password_err = ''
    verify_password_err = ''
    username_err = ''

    if username == "":
        username_err = 'please stay between 3 and 30'
    if password == "":
        password_err = 'please stay between 3 and 30'
    if verify_password == "":
        verify_password_err = 'your password does not match'

    if len(username) < 3:
        username = ''
        username_err = 'please stay between 3 and 30'
    elif len(username) > 30:
        username = ''
        username_err = 'please stay between 3 and 30'
    else:
        username = username

    if len(email) > 0:
        if not(email.endswith('@') or email.startswith('@') or email.endswith('.') or email.startswith('.')) and email.count('@') == 1 and email.count('.') == 1:
            email = email
        else:
            email = ''
            email_err = 'try again - this is not a common email address'
    else:
        email = ''


    if len(password) > 30 :
        password = ''
        password_err = 'please stay between 3 and 30'
    elif len(password) < 3:
        password = ''
        password_err = 'please stay between 3 and 30'

    if password != verify_password:
        password = ''
        verify_password = ''
        verify_password_err = 'your password does not match'
    else:
        verify_password = verify_password


    if not username_err and not password_err and not verify_password_err and not email_err:
        return render_template('welcome.html', name = username)

    else:
        return render_template('inputs.html', email_err=email_err, password_err=password_err, verify_password_err=verify_password_err, username_err=username_err,
        email=email, password=password, verify_password=verify_password,username=username )


app.run()
