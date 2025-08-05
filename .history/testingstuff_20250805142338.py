import json
import random


def register(username, password):
    newUser = {'username': username, 'password': password, 'userID': random.randint(1,1000)}
    try:
        with open('users.json', 'r') as f:
            json.dump("users"[newUser], f, indent=4)
    except Exception as e:
        print(e)

register('diyar', 'password123')