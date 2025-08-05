import json
import random

def userID()

def register(username, password):
    newUser = {'username': username, 'password': password}
    try:
        with open('users.json', 'a') as f:
            json.dump(newUser, f, indent=4)