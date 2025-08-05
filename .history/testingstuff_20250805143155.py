import json
import random


def register(username, password):
    newUser = {'username': username,
                'password': password, 
                'userID': lambda id = 
                }
    try:
        with open('users.json', 'r') as file:
                users = json.read(file)
    except (FileNotFoundError, json.JSONDecodeError) :
        users = []

register('diyar', 'password123')