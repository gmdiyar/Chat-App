import json
def register(username, password):
    
    try:
        with open('users.json', 'a') as f:
            json.dump(newUser, f, indent=4)