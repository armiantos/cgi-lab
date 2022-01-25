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
    Adds the Set-Cookie headers for username and password to the HTTP response if not already set.
    Must be called before the final CRLF before the message body.
    """
    cookie = SimpleCookie(os.environ['HTTP_COOKIE'])

    if cookie.get('username'):
        cookie.get('username').clear()
    print(f'Set-Cookie: username={username}')

    if cookie.get('password'):
        cookie.get('username').clear()
    print(f'Set-Cookie: password={password}')


s = cgi.FieldStorage()

# Question 4
form_username = s.getfirst('username')
form_password = s.getfirst('password')

# Question 5
if os.environ['REQUEST_METHOD'] == 'POST' and is_authenticated(form_username, form_password):
    set_username_password_cookies(form_username, form_password)

print('Content-Type: text/html')
print()

if is_authenticated(form_username, form_password):
    print(secret_page(username=form_username, password=form_password))
else:
    print(login_page())
