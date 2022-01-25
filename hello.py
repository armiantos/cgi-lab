#!/usr/bin/env python3

import json
import os

print('Content-Type: text/html')
print()

payload = {
    # Question 1
    'environment_variables': dict(os.environ),
    # Question 2
    'query_parameter': os.environ['HTTP_USER_AGENT'],
    # Question 3
    'browser_info': os.environ['HTTP_USER_AGENT']
}

for section_title, contents in payload.items():
    print(f'''
    <h1>{section_title}</h1>
    <pre>{contents}</pre>
    ''')
