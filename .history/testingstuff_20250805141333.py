import json
with open('users.json', 'w') as file:
                newUser = {'user1': 'username', 'password': '13123123'}
                json.dump(newUser, file, indent=4)
