#!/usr/bin/env python3

import ssl, json, requests, pwinput

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
    nacserver = input('Enter NAC Server IP: ')
    apikey = input('Enter NAC API Key: ')
    newuser = input('Enter New User Name: ')
    newpass = pwinput.pwinput(prompt='Please enter your New User password: ')
    setuser(nacserver, apikey, newuser, newpass)
