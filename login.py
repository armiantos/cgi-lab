#!/usr/bin/env python3

import cgi
from http.cookies import SimpleCookie
from templates import login_page

s = cgi.FieldStorage()
username = s.getfirst('username')
password = s.getfirst('password')

print('Content-Type: text/html')
print()

print(login_page())
if username and password:
    print(username, password)
