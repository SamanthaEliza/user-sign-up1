from flask import Flask, request, redirect, render_template

import cgi
import os

app= Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_user_signup():
    return render_template('html_user_signup1.html')

def empty_val(value):
    if len(value) < 1:
        return True
    else:
        return False

def charater_length(value):
    if len(value) > 2 and len(value) < 21:
        return True
    else:
        return False

def email_symbols(email):
    if "@" not in email:
        return False
    else:
        return True

def email_dot(email):
    if "." not in email:
        return False
    else:
        return True

@app.route('/user-signup', methods=['POST'])
def user_signup():


    username = request.form['username']
    password = request.form['password']
    password_check = request.form['verify']
    email = request.form['email']


    username_error = ''
    password_error = ''
    password_check_error = ''
    email_error = ''

    error_required = "Required field"
    error_re_enter_password = "Please re-enter password"
    error_chara_count = "must be between 3 and 20 characters"
    error_no_spaces = "must not contain spaces"


    if empty_val(password):
        password_error = error_required
        password = ''
        password_check = ''
    if not charater_length(password):
        password_error = "Password " + error_chara_count
        password = ''
        password_check = ''
        password_check_error = error_re_enter_password
    
    if " " in password:
        password_error = "Password " + error_no_spaces
        password = ''
        password_check = ''
        password_check_error = error_re_enter_password


    if password_check != password:
        password_check_error = "Passwords must match"
        password = ''
        password_check = ''
        password_error = 'Passwords must match'
            

    if empty_val(username):
        username_error = error_required
    if not charater_length(username):
        username_error = "Username " + error_chara_count

    if " " in username:
        username_error = "Username " + error_no_spaces



    if not empty_val(email):
        
        if not charater_length(email):
            email_error = "Email " + error_chara_count
           
        elif not email_symbols(email):
            email_error = "Email must contain the @ symbol"
        
        elif not email_dot(email):
            email_error = "Email must contain ."
        
        elif " " in email:
            email_error = "Email " + error_re_enter_password
           


    if not username_error and not password_error and not password_check_error and not email_error:
       # return redirect('/welcome?username={0}'.format(username))
        return render_template('main.html', username=username)
    else:
        return render_template('html_user_signup1.html', username_error=username_error, username=username, password_error=password_error, password=password, email_error=email_error, email=email, password_check=password_check,password_check_error=password_check_error)


@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('main.html', username=username)

app.run()