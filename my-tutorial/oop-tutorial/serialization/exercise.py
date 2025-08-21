import json

def process_json(data: dict, filename: str) -> dict:
    """
    Serializes a dictionary to a JSON file and then 
    deserializes it back to a dictionary.

    Args:
        data (dict): The dictionary to process.
        filename (str): The filename for the JSON file.

    Returns:
        dict: The deserialized dictionary from the JSON file.
    """
    # Serialize dictionary to JSON file
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    # Deserialize JSON file back into a dictionary
    with open(filename, 'r') as f:
        deserialized_data = json.load(f)

    return deserialized_data


sample_data = {"name": "Billy", "age": 19, "skills": ["Python", "React"]}
result = process_json(sample_data, "output.json")

print(result)
# Output: {'name': 'Billy', 'age': 19, 'skills': ['Python', 'React']}
