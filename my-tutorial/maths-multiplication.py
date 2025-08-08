def main():
    user_input = multiply(int(input("Enter any number to get it's multiplication table: ")))
    return user_input

def multiply(x):
    for i in range(1, 20):
        print(f"{x} * {i} = {x*i}")

main()