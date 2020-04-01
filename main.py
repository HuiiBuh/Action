
import json
with open('/home/runner/work/Action/Action/cookies.json') as file:
    a = file.read()
    print(a.replace(" ", ""))
    cookie = json.load(file)
    cookies = SpotifyCookies(cookie['sp_t'], cookie['sp_dc'], cookie['sp_key'])
