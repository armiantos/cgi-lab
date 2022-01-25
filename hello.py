#!/usr/bin/env python3

import os

print('Content-Type: text/html')
print()
print(f"<p>{os.environ['HTTP_USER_AGENT']}</p>")
