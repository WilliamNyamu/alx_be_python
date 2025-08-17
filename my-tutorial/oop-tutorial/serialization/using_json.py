"""
    The json module is used for serializing and deserializing data to and from the JSON
    format, which is human-readable and widely used for data interchange.
"""
import json

#Sample Python object
data = {'name' : 'Alice', 'age' : 30, 'city': 'Kampala'}

# Serialize the object to a JSON string
json_string = json.dumps(data)

# Optionally, write the JSON string to a file
with open('data.json', 'w') as file:
    json.dump(data, file)

# Here, the dictionary data is converted to a JSON string and also
# written to a file named data.json

