#!/usr/bin/env python3

import cgi
import secret
from templates import login_page, secret_page

s = cgi.FieldStorage()
username = s.getfirst('username')
password = s.getfirst('password')


def is_authenticated() -> bool:
    return secret.username == username and secret.password == password


print('Content-Type: text/html')
print()

# Question 4
if is_authenticated():
    print(secret_page(username=username, password=password))
else:
    print(login_page())
