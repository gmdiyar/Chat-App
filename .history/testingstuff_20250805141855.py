import json
def register(username, password):
    newUser = {'username'}
    try:
        with open('users.json', 'a') as f:
            json.dump(newUser, f, indent=4)