import json

# Deserialize the JSON string back into a Python object
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)

# This code converts the JSON string back into a Python dictionary
# and demonstrates how to read and deserialize data from a JSON file.

