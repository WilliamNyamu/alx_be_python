# The try and except statements are the primary method of 
# dealing with exceptions

# try:
#   # Code that might raise an exception
# except ExceptionType:
#   # Code to handle the exception
# else:
#   # Code that executes if no exception occurs
# finally:
#   # Code that always executes, regardless of exceptions


x = 0
try: 
    print(5/x)
except ZeroDivisionError:
    print("Something went wrong")

# We have 3 possibilities when dealing with try and except statements

# 1. No errors in the try clause:

# Execute the try clause
# Skip all except clauses
# Continue running as normal

y = 1
try:
    print(5/y)
except ZeroDivisionError:
    print("Something went wrong!")

print("I am executing after the try clause")

# 2. Errors in the try clause and the exception is specified
# The program will:
# Skip the remaining code in the try clause
# Execute any code in the matching except clause\
# Continue running as normal

z = 0
try:
    print(5/z)
except ZeroDivisionError:
    print("You divided a number by 0")
print("Now I continue running the code")

# 3. Errors in the try clause and the exception is not specified
# -> If the program throws an exception in the try clause, 
# but the exception is not specified in any except statements, 
# the program will stop the execution of the program and throw the error

w = 0
try:
    print(5/w) #Notice that I am not using w
except:
    print("An error occurred, but I don't know what it is")

# In the above example, I am trying to divide 5 by the varibale v which doesn;t exist
# This raises a NameError

# Final clause(optional)
# The final clause will always execute whether 
# there is an error or not

k = 1
try:
    print(5/k)
except ZeroDivisionError:
    print("I am the except clause")
finally: 
    print("I am the finally clause")

print("I am the after try clause execution")

# The finally clause is useful for cleaning up resources
# Actions such as closing connections, closing files, 
# and logging are great candidates for finally clause

# Conditional Execution with the Else Clause
# The other optional clause is the else clause.
# If the code in the try clause executes without throwing 
# an error,then the code in the else clause will also execute

i = 1
try:
    print(5/i)
except ZeroDivisionError:
    print("Divided a number by zero")
else:
    print("I am the else clause")
finally:
    print("I am the finally clause")

# If we experience an exception or error in the try clause, 
# the else clause would be ignored

