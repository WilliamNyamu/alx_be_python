#It is a sequence of key-value pairs, separated by a comma and surrounded by curly braces.
# It's similar to JavaScript's objects 
# basic syntax is shown below:

# demo_dict = {
#     "key": "value",
#     "key": "value",
#     "key": "value"
# }

first_dict = {
    "name": "freeCodeCamp",
    "founder": "Quinty Larson",
    "type": "charity",
    "age": 8,
    "price": "free",
    "work-style": "remote"
}

# Use the get method to retrieve the value of a key
founder = first_dict.get("founder")
print(f"The founder os freeCodeCamp is {founder} ")

# The items() method returns all the entries of the dictionary in a list
# In the list, is a tuple representing all each entry

items = first_dict.items()
print(items)

# The keys() method returns all the keys in the dictionary. The keys are returned in a tuple
keys = first_dict.keys()
print(keys)

# The values() method returns all the values in the dictionary. It is returned in a tuple

values = first_dict.values()
print(values)

# The pop() method removes a key-value pair from the dictionary. To make it work, include the key to be removed
pop = first_dict.pop("work-style")
print(first_dict)

# The popitem() method works like the pop() method. The difference is that it removes the last item in the dictionary.
last_pop = first_dict.popitem()
print(first_dict)

# The update() method adds an item to the dictionary. 
# You have to specify both the key and value inside its braces and surround it with curly braces.

first_dict.update({"Editor" : "Abbey Rennemeyer"})
print(first_dict)

# The copy() method copies the dictionary into the variable specified.
second_dict = first_dict.copy()
print(second_dict)

second_dict.update({"Employee" : "William Nyamu"})
print(second_dict)

# The clear() method removes all entries in the dictionary.
first_dict.clear()
print(first_dict)


# Practice test
# A script to determine voting.