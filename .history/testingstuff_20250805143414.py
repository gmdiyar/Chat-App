import json
import random


def userID

def register(username, password):
    newUser = {'username': username,
                'password': password, 
                'userID': newID 
                }
    try:
        with open('users.json', 'r') as file:
                users = json.read(file)
    except (FileNotFoundError, json.JSONDecodeError) :
        users = []

register('diyar', 'password123')