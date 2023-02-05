# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# sample json 
zukJSON = '{"first_name": "ZUK", "last_name": "J", "age": 30}'

# pars to dict

user = json.loads(zukJSON)

print(user['first_name'])
print(user)
car = {'make': 'Ford', 'model': 'mustung', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)