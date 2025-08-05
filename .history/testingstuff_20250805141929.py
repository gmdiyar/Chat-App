import json
import random

def userID():
    ID = random.

def register(username, password):
    newUser = {'username': username, 'password': password}
    try:
        with open('users.json', 'a') as f:
            json.dump(newUser, f, indent=4)