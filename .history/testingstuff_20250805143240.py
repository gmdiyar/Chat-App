import json
import random


def register(username, password):
    newUser = {'username': username,
                'password': password, 
                'userID': lambda id = random.randint(1,1000) if id not in users else  
                }
    try:
        with open('users.json', 'r') as file:
                users = json.read(file)
    except (FileNotFoundError, json.JSONDecodeError) :
        users = []

register('diyar', 'password123')