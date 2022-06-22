#!/usr/bin/env python3

import requests
import sys
import json
from getpass import getpass

requests.packages.urllib3.disable_warnings()

def main():
    ip_address = input("What is the IP address of your CML server? ")
    cml_url = f"https://{ip_address}/api/v0/"
    username = "admin"
    password = getpass("Please enter your password: ")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    token = auth(cml_url, username, password, headers)
    users = getUsers(cml_url, token)
    displayUsers(users)

def auth(cml_url, username, password, headers):
    url = cml_url + "authenticate"
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)
    response_json = response.json()
    # print(response_json)
    return(response_json)


def getUsers(cml_url, token):
    url = cml_url + "users"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url=url, headers=headers, verify=False)
    response_json = response.json()
    # print(response_json)
    return(response_json)


def displayUsers(users):
    # print(users)
    for user in users:
        print("User: " + user)


if __name__ == "__main__":
    sys.exit(main())
