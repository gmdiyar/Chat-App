import json
import random


def register(username, password):
    newUser = {'username': username, 'password': password, 'userID': random.randint(1,1000)}
    # try:
    with open('users.json', 'w') as f:
            json.dump(newUser, f)

    # except Exception as e:
    #     print(e)

register('diyar', 'password123')