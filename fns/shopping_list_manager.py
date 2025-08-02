def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item_add = input("Add item: ")
            shopping_list.append(item_add)
            pass
        elif choice == '2':
            item_remove = input("Choose item to remove: ")
            shopping_list.remove(item_remove)
            pass
        elif choice == '3':
            for item in shopping_list:
                print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == '__main__':
    main()
