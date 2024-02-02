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
    #nac servers and api key need to be set here
    naclist = [
        {
            'ip': '',
            'key': ''
        },
        {
            'ip': '',
            'key': ''
        },
        {
            'ip': '',
            'key': ''
        }
    ]

    newuser = input('Enter New User Name: ')
    newpass = pwinput.pwinput(prompt='Please enter your New User password: ')

    for pod in naclist:
        setuser(pod['ip'], pod['key'], newuser, newpass)

