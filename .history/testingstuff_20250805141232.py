import json
with open('users.json', 'a') as file:
                newUser = [1,2,3]
                json.dump(newUser, file, indent=4)
