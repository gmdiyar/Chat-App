import json
try:
    with open('users.json', 'w') as file:
        newUser = {'user1': 'username', 'password': '131123'}
        json.dump(newUser, file, indent=4)
