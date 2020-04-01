
import json
import logging

with open('/home/runner/work/Action/Action/cookies.json') as file:
    text = file.read()
    print(text)
    print(text.replace(" ", ""))
    cookie = json.loads(text)
    cookie = json.load(file)
    print(cookie)
