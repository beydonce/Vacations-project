import re
from datetime import datetime
<<<<<<< HEAD
from logic.user_logic import UserLogic
=======
>>>>>>> d81b1a82505bc01d37a0de0e7de0a6779a52c964

class UserFacade:
    def __init__(self):
        self.logic = UserLogic()

    def display_all_users(self):
        users = self.logic.get_all_users()
        for user in users:
            print(user)

    def register_user(self):
<<<<<<< HEAD
        # Username validation
        while True:
            username = input("Enter username: ")
            if username.isalnum():
                break
            else:
                print("Invalid username. Please use only letters and numbers.")

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

        # Role ID validation
        while True:
            try:
                role_id = int(input("Enter role ID (1 for admin, 2 for user): "))
                if role_id in [1, 2]:
                    break
                else:
                    print("Invalid role ID. Choose 1 for admin or 2 for user.")
            except ValueError:
                print("Role ID must be an integer.")

        # Add user after all validations pass
        self.logic.add_user(username, first_name, last_name, email, password, date_of_birth, role_id)
=======
        # Validate first name and last name
        first_name = input("Enter first name: ")
        if not first_name.isalpha():
            print("Invalid first name. Please enter only letters.")
            return

        last_name = input("Enter last name: ")
        if not last_name.isalpha():
            print("Invalid last name. Please enter only letters.")
            return

        # Validate email format using regex
        email = input("Enter email: ")
        if not self.is_valid_email(email):
            print("Invalid email format.")
            return

        password = input("Enter password: ")
        if len(password) < 6:
            print("Password must be at least 6 characters long.")
            return

        # Validate date of birth format
        d_o_b = input("Enter date of birth (YYYY-MM-DD): ")
        if not self.is_valid_date(d_o_b):
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        # Validate role ID
        try:
            role_id = int(input("Enter role ID (1 for admin, 2 for user): "))
            if role_id not in [1, 2]:
                print("Invalid role ID. Choose 1 for admin or 2 for user.")
                return
        except ValueError:
            print("Role ID must be an integer.")
            return

        # If all validations pass, add the user
        self.logic.add_user(first_name, last_name, email, password, d_o_b, role_id)
>>>>>>> d81b1a82505bc01d37a0de0e7de0a6779a52c964
        print("User registered successfully!")

    def delete_user(self):
        try:
            user_id = int(input("Enter user ID to delete: "))
            self.logic.delete_user(user_id)
            print("User deleted successfully!")
        except ValueError:
            print("Invalid user ID. Please enter an integer.")

<<<<<<< HEAD
    def login(self, username, password):
        """
        Method to validate user login credentials.
        """
        user = self.logic.get_user_by_username(username)  # Fetch user details
        if user and user['password'] == password:  # Compare passwords using dictionary keys
            print(f"Welcome back, {username}!")
            return user  # Return user dictionary or relevant info
        else:
            print("Invalid username or password.")
            return None

=======
    def login_user(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        user = self.logic.get_user_by_email(email)
        if user and user.password == password:
            print("Login successful!")
            return user  # Return the user object or relevant info after successful login
        else:
            print("Invalid email or password!")
            return None  # Return None or handle invalid login attempt
>>>>>>> d81b1a82505bc01d37a0de0e7de0a6779a52c964

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
