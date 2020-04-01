
import json
import logging

with open('/home/runner/work/Action/Action/cookies.json') as file:
    text = file.read()
    cookie = json.loads(text)
    print(cookie)
