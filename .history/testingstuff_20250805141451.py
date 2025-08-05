import json
with open('users.json', 'a+') as file:
                newUser = {'user1': 'username', 'password': '131123'}
                json.dump(newUser, file, indent=4)
