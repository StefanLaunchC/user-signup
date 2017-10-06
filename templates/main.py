from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/', methods=['POST'])
def user_signup():

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ''
    password_error = ''
    verifypassword_error = ''
    email_error = ''

    if(len(username)<3):
        username_error = "Username is too short"

    if password!=verify:
        verifypassword_error = "Password does not match"

    if len(email) > 0 and ((email.count ("@") != 1) or (email.count(".") !=1) or (email.count (" ") !=0) or 
            (len(email) < 3) or (len(email) > 20)):
        email_error = "Please enter a valid emailaddress" 
        return render_template("index.html", email_error=email_error)
    
        
    

        

    return render_template('signup.html', username=username, email=email)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)



app.run()