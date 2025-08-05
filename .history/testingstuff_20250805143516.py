import json
import random


def userIDGenerator():
     return random.randint(1,1555)

def register(username, password):
    newUser = {'username': username,
                'password': password, 
                'userID': userIDGenerator()
                }
    try:
        with open('users.json', 'r') as file:
                users = json.read(file)
    except (FileNotFoundError, json.JSONDecodeError) :
        users = []
    users.append(newUser)
    json.dump(users)
register('diyar', 'password123')