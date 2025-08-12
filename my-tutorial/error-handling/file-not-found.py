# Error handling when filenotfound.
# Requires knowledge in file handling.

class CustomFileNotFoundError(Exception):
    """Exception handling when file not found"""
    def __init__ (self, file_name):
        self.file_name = file_name
    
    def __str__ (self):
        return f"Error: File '{self.file_name}' not found."

def file_open():
    user_file_name = input("Enter the file name: ").strip()
    name_list = [user_file_name]
    name_list.append('txt')
    user_file = '.'.join(name_list)
    try:
        with open(user_file) as f_name:
            count = 0
            for _ in f_name:
                count += 1
        return f"You've successfully opened '{user_file}'. It has {count} lines"
    except FileNotFoundError:
        raise CustomFileNotFoundError(user_file)

try:
    print(file_open())
except CustomFileNotFoundError as e:
    print(e)
finally:
    print("It's all good!")


