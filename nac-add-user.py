#!/usr/bin/env python3

import ssl, json, requests, pwinput, yaml, sys
from yaml.loader import SafeLoader

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings() 
sys.tracebacklimit = 0

def setuser(nacserver, apikey, newuser, newpass, fname, lname, email):
    headers = {
        'Authorization': 'Bearer {}'.format(apikey),
        'Content-Type': 'application/json'
    }

    url = 'https://{}:8443/api/v2/user'.format(nacserver)

    data = {
        'userID': '{}'.format(newuser),
        'password': '{}'.format(newpass),
        'firstName': '{}'.format(fname),
        'lastName': '{}'.format(lname),
        'email': '{}'.format(email),
        'adminProfileId': 1,
        'type': 46,
        'adminUser': True
    }

    try:
        req = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False, timeout=10)
        if req.status_code == 409:
            print('User account already exist on Pod {}'.format(nacserver))
        elif req.status_code != 201:
            print('Unable to connect to Pod {} error number {}'.format(nacserver, req.status_code))
        else:
            return
    except requests.ConnectionError:
        print('Server {} did not respond'.format(nacserver))

if __name__ == '__main__':
    #nac servers and api key need to be set here
    with open('pods.yml', 'r') as pods:
        naclist = list(yaml.load_all(pods, Loader=SafeLoader))

    fname = input('Enter New Users First Name: ')
    lname = input('Enter New Users Last Name: ')
    email = input('Enter New Users Email Address: ')
    newuser = input('Enter New User ID: ')
    newpass = pwinput.pwinput(prompt='Please enter your New User password: ')
    
    for pods in naclist:
        for k, v in pods['pods'].items():
            if v['ip'] != None:
                setuser(v['ip'], v['key'], newuser, newpass, fname, lname, email)