import re
from datetime import datetime
from logic.user_logic import UserLogic

class UserFacade:
    def __init__(self):
        self.logic = UserLogic()

    def display_all_users(self):
        users = self.logic.get_all_users()
        if users:
            print("\n" + "=" * 50)
            print(f"{'ID':<5} {'Username':<15} {'First Name':<15} {'Last Name':<15} {'Role':<10}")
            print("-" * 50)
            for user in users:
                role = "Admin" if user['role_id'] == 1 else "User"
                print(f"{user['id']:<5} {user['username']:<15} {user['first_name']:<15} {user['last_name']:<15} {role:<10}")
            print("=" * 50)
        else:
            print("\nNo users found.")

        # Pause to let the admin view the list
        input("\nPress Enter to return to the menu...")


    def register_user(self):
        # Username validation
        while True:
            username = input("Enter username: ")
            if not username.isalnum():
                print("Invalid username. Please use only letters and numbers.")
                continue
            if self.logic.get_user_by_username(username):
                print("Username already taken. Please choose another.")
                continue
            break

        # First name validation
        while True:
            first_name = input("Enter first name: ")
            if first_name.isalpha():
                break
            else:
                print("Invalid first name. Please enter only letters.")

        # Last name validation
        while True:
            last_name = input("Enter last name: ")
            if last_name.isalpha():
                break
            else:
                print("Invalid last name. Please enter only letters.")

        # Email validation
        while True:
            email = input("Enter email: ")
            if self.is_valid_email(email):
                break
            else:
                print("Invalid email format.")

        # Password validation
        while True:
            password = input("Enter password: ")
            if len(password) >= 6:
                break
            else:
                print("Password must be at least 6 characters long.")

        # Date of birth validation
        while True:
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            if self.is_valid_date(date_of_birth):
                break
            else:
                print("Invalid date format. Please use YYYY-MM-DD.")

        # Set role_id to 2 (User) by default
        role_id = 2  

        # Add user after all validations pass
        self.logic.add_user(username, first_name, last_name, email, password, date_of_birth, role_id)
        print("User registered successfully!")


    def delete_user(self):
        try:
            user_id = int(input("Enter user ID to delete: "))
            self.logic.delete_user(user_id)
            print("User deleted successfully!")
        except ValueError:
            print("Invalid user ID. Please enter an integer.")

    def login(self, username, password):
        """
        Method to validate user login credentials.
        """
        user = self.logic.get_user_by_username(username)  # Fetch user details
        if user and user['password'] == password:  # Compare passwords using dictionary keys
            print(f"Welcome back, {username}!")
            return user  # Return the user dictionary (including id and role)
        else:
            print("Invalid username or password.")
            return None


    def is_valid_email(self, email):
        # Simple email validation regex
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def is_valid_date(self, date_str):
        # Validate date format (YYYY-MM-DD)
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False
