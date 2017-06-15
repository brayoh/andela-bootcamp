import requests
import pprint
import json
username = input("please enter your github username to get started: ")


def fetch_repos(username):
    print("\u2592 \n  *** fetching repos...please wait")
    url = "https://api.github.com/users/{}/repos".format(username)
    repos = requests.get(url).json()

    print(pprint.pprint(repos))
    print('\u2592 *** {} repos found for account with username {} *** \u2713'.format(len(repos), username,));

if username:
    url = "https://api.github.com/users/{}".format(username)
    user = requests.get(url)
    if user.status_code == 200:
        print("\u2592 *** user found *** \u2713 ");
        fetch_repos(username)
