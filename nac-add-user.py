#!/usr/bin/env python3

import ssl, json, requests, pwinput, yaml, pprint
from yaml.loader import SafeLoader

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings() 

def setuser(nacserver, apikey, newuser, newpass):
    headers = {
        'Authorization': 'Bearer {}'.format(apikey),
        'Content-Type': 'application/json'
    }

    url = 'https://{}:8443/api/v2/user'.format(nacserver)

    data = {
        'userID': '{}'.format(newuser),
        'password': '{}'.format(newpass),
        'adminProfileId': 1,
        'type': 46,
        'adminUser': True
    }

    req = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)
    print(req.status_code)

if __name__ == '__main__':
    #nac servers and api key need to be set here
    with open('pods.yml', 'r') as pods:
        naclist = list(yaml.load_all(pods, Loader=SafeLoader))

    newuser = input('Enter New User Name: ')
    newpass = pwinput.pwinput(prompt='Please enter your New User password: ')

    for pods in naclist:
        for k, v in pods['pods'].items():
            if v['ip'] != None:
                setuser(v['ip'], v['key'], newuser, newpass)