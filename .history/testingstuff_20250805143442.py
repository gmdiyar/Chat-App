import json
import random


def userIDGenerator():
     return

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

register('diyar', 'password123')