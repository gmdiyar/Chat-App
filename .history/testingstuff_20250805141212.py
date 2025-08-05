import json
with open('users.json', 'a') as file:
                json.dump(newUser, file, indent=4)
                