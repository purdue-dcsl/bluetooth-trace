import json

with open('trace.json', 'r') as f:
    data = json.load(f)

print(f'{len(data)} users')

for user_id, values in data.items():
    print(f'one user id: {user_id}')
    print(f'user data fields: {values[0].keys()}')
    exit()
