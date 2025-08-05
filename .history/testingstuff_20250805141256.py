import json
with open('users.json', 'a') as file:
                newUser = {'user1': 'username'}
                json.dump(newUser, file, indent=4)
