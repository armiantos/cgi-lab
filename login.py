#!/usr/bin/env python3

import cgi
from http.cookies import SimpleCookie
import os
import secret
from templates import after_login_incorrect, login_page, secret_page


def is_authenticated(username, password) -> bool:
    return secret.username == username and secret.password == password


def set_username_password_cookies(username, password):
    """
    Adds the Set-Cookie headers for username and password.
    Must be called before the final CRLF before the message body.
    """
    print(f'Set-Cookie: username={username}')
    print(f'Set-Cookie: password={password}')


s = cgi.FieldStorage()
cookie = SimpleCookie(os.environ['HTTP_COOKIE'])

# Question 4
form_username = s.getfirst('username')
form_password = s.getfirst('password')

cookie_username = cookie.get(
    'username').value if cookie.get('username') else None
cookie_password = cookie.get(
    'password').value if cookie.get('password') else None

# Question 5
if os.environ['REQUEST_METHOD'] == 'POST' and is_authenticated(form_username, form_password):
    set_username_password_cookies(cookie, form_username, form_password)

# Autofill form data from cookie
if cookie_username is not None and cookie_password is not None:
    form_username = cookie_username
    form_password = cookie_password

print('Content-Type: text/html')
print()

if is_authenticated(form_username, form_password):
    print(secret_page(username=form_username, password=form_password))
elif os.environ['REQUEST_METHOD'] == 'POST' and not is_authenticated(form_username, form_password):
    print(after_login_incorrect())
else:
    print(login_page())
