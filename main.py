
import json
import logging

with open('/home/runner/work/Action/Action/cookies.json') as file:
    text = file.read()
    print(text.replace(" ", ""))
    cookie = json.loads(text)
    cookies = SpotifyCookies(cookie['sp_t'], cookie['sp_dc'], cookie['sp_key'])
