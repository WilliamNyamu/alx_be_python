# ValueTooHighError exception if the number is greater than 100
class ValueTooHighError(Exception):
    """Exception handling when the value is higher than 100"""
    def __init__ (self, num):
        self.num = num
    
    def __str__ (self):
        return f"Error: The number {self.num} is higher than 100 by {self.num - 100}"

def put_number():
    user_num = int(input("Enter a number: "))
    if user_num > 100:
        raise ValueTooHighError(user_num)
    else:
        return f"The number '{user_num}' is good!"

try:
    print(put_number())
except ValueTooHighError as e:
    print(e)
finally:
    print("Finished my job!")

    