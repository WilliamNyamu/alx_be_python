# In any programming language, functions facilitate code reusability. 
# In simple terms, when you want to do something repeatedly, 
# you can define that something as a function and 
# call that function whenever you need to.

def greet():
    print("Hello, hope you are doing well!")

# The above function is inert unless it is called
greet() # The function takes no arguments, returns nothing, prints whenever it's called.

def my_func(name,place):
    print(f"Hello {name}. Are you from {place}?")

my_func("Jane", "Paris")
# The arguments in the my_func call are positional arguments. This means that the first argument
# in the function call is used as the value for the first parameter.

my_func(name='Robert', place='Hawaii')
# The arguments here are called keyword arguments

def total_calc(bill_amount, tip_perc=10):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

# When you call the function total_calc with only the bill_amount, 
# by default the tip percentage of 10 is used.
# When you explicitly specify the percentage tip, 
# the tip percentage mentioned in the function call is used.

#specify only bill_amount
total_calc(150)
#specify both the bill_amount and a custom tip percentage
total_calc(200, 15)


def volume_of_cuboid(height, length, width):
    return length*height*width

# Recall that the return keyword returns control to the point where the function was called.
# The function call is replaced with the return value from the function

volume = volume_of_cuboid(5.5, 20, 6)
print(f"Volume of the cuboid is {volume} cubic units")

# To return multiple values from a function, 
# just specify the values to be returned, separated by a comma.
# By default, the function returns the values as a tuple.

def cube(side):
    volume = side**3
    surface_area = 6 * (side ** 2)
    return volume, surface_area

returned_values = cube(8)
print(returned_values)

# Unpack the tuple and store the values in two different variables.

cube_volume, cube_area = cube(6.5)
print(f"Volume of the cube is {cube_volume} cubic units and the total surafe area is {cube_area} sq. units ")

#Creating a function that takes a variable number of arguments
def my_var_sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
# Notice how the function definition now has *args 
# instead of just the name of the parameter. 
# In the body of the function, we loop through args until 
# we've used all the arguments. The function my_var_sum 
# returns the sum of all numbers passed in as arguments.

# Example 1 with 4 numbers
sum = my_var_sum(99, 10, 54, 23)
print(f"The numbers that you have add up to {sum}")
# Example 2 with 6 numbers
another_sum = my_var_sum(11, 22, 33, 44, 55, 66)
print(f"The second set of numbers add up to {another_sum}")

def even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

user_number = int(input("Please enter a number: "))

result =  even_or_odd(user_number)
print(result)