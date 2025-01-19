import sys
import os
from dal import DAL

# Add project path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from facade.user_facade import UserFacade
from facade.countries_facade import CountryFacade
from facade.vacations_facade import VacationFacade
from facade.likes_facade import LikesFacade
from facade.roles_facade import RolesFacade


def show_welcome_screen():
    print("\n" + "=" * 60)
    print("""  
    ██╗   ██╗ █████╗  ██████╗██╗ █████╗ ████████╗ █████╗  ██████╗ ███╗   ██╗
    ██║   ██║██╔══██╗██╔════╝██║██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║
    ██║   ██║███████║██║     ██║███████║   ██║   ███████║██║   ██║██╔██╗ ██║
    ╚██╗ ██╔╝██╔══██║██║     ██║██╔══██║   ██║   ██╔══██║██║   ██║██║╚██╗██║
     ╚████╔╝ ██║  ██║╚██████╗██║██║  ██║   ██║   ██║  ██║╚██████╔╝██║ ╚████║
      ╚═══╝  ╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
    """)
    print("=" * 60)
    print("""
    🌴 Welcome to the Vacation Management System 🌴

    Let's log in or sign up to get started!
    """)
    print("=" * 60)


def login_or_signup():
    while True:
        print("=== Authentication ===")
        print("1. Log In")
        print("2. Sign Up")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user, role = log_in(username, password)  # Pass both username and password
            return role  # Return the user role (admin or user)
        elif choice == '2':
            user_facade = UserFacade()
            user_facade.register_user()
        elif choice == '0':
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")


def log_in(username, password):
    user_facade = UserFacade()
    user = user_facade.login(username, password)  # Correct method call

    if user:
        # Assuming the role is stored in the user object as 'role_id'
        role = user['role_id']  # Fetch role_id from the user data
        if role == 1:  # If the user is an admin
            return user, "admin"
        elif role == 2:  # If the user is a regular user
            return user, "user"
        else:
            return user, "user"  # Default role if role_id is unrecognized
    else:
        print("Invalid login credentials.")
        return None, None  # Return None for both user and role


def sign_up():
    print("\n--- Sign Up ---")
    user_facade = UserFacade()

    # Register a new user
    user_facade.register_user()

    print("You are successfully registered!")
    return "user"  # Default role for new users


def main_menu(user_role):
    while True:
        print("\n=== Main Menu ===")
        if user_role == "admin":
            print("1. Manage Users 👥")
            print("2. Manage Countries 🌍")
            print("3. Manage Vacations 🏖️")
            print("4. Manage Likes ❤️")
            print("5. Manage Roles 👔")
        else:
            print("1. View Vacations 🏖️")
            print("2. Like Vacations ❤️")
            print("3. View Countries 🌍")
        print("0. Exit 🚪")

        choice = input("Choose an option: ")

        if user_role == "admin":
            if choice == "1":
                manage_users()
            elif choice == "2":
                manage_countries()
            elif choice == "3":
                manage_vacations()
            elif choice == "4":
                manage_likes()
            elif choice == "5":
                manage_roles()
            elif choice == "0":
                break
            else:
                print("\nInvalid choice. Please try again!")
        else:
            if choice == "1":
                manage_vacations()
            elif choice == "2":
                manage_likes()
            elif choice == "3":
                manage_countries()
            elif choice == "0":
                break
            else:
                print("\nInvalid choice. Please try again!")


def main():
    show_welcome_screen()
    user_role = login_or_signup()
    if user_role:  # Proceed only if user_role is valid (not None)
        main_menu(user_role)


if __name__ == "__main__":
    main()
