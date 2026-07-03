import json
import os

FILE_NAME = "users.json"

def load_users():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)

def login():
    users = load_users()

    username = input("Enter Username: ")

    if username not in users:
        print("User not found.")
        return

    if users[username]["locked"]:
        print("Account is locked due to multiple failed login attempts.")
        return

    password = input("Enter Password: ")

    if password == users[username]["password"]:
        print("\nLogin Successful!")
        users[username]["attempts"] = 0
    else:
        users[username]["attempts"] += 1

        remaining = 3 - users[username]["attempts"]

        if users[username]["attempts"] >= 3:
            users[username]["locked"] = True
            print("\nAccount Locked!")
        else:
            print(f"\nWrong Password.")
            print(f"Remaining Attempts: {remaining}")

    save_users(users)

def reset_account():
    users = load_users()

    username = input("Username to Reset: ")

    if username in users:
        users[username]["attempts"] = 0
        users[username]["locked"] = False
        save_users(users)
        print("Account Reset Successfully.")
    else:
        print("User not found.")

while True:

    print("\n==============================")
    print(" LOGIN ATTEMPT CONTROL SYSTEM")
    print("==============================")
    print("1. Login")
    print("2. Reset Account")
    print("3. Exit")

    choice = input("Choose Option: ")

    if choice == "1":
        login()

    elif choice == "2":
        reset_account()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice.")
