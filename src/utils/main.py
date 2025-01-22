# main.py

from facade.user_facade import UserFacade
from facade.vacations_facade import VacationFacade
from facade.likes_facade import LikesFacade

vacation_facade = VacationFacade()
likes_facade = LikesFacade()

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
            user, role = log_in(username, password)
            if user:
                return user, role  # Return both the user and role
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
    user = user_facade.login(username, password)

    if user:
        role = user['role_id']  # Fetch role_id from the user data
        if role == 1:
            return user, "admin"
        elif role == 2:
            return user, "user"
        else:
            return user, "user"
    else:
        print("Invalid login credentials.")
        return None, None


def manage_vacations():
    while True:
        print("\n=== Manage Vacations ===")
        print("1. Add New Vacation 🏖️")
        print("2. Update Vacation Details 📝")
        print("3. Delete Vacation 🗑️")
        print("0. Back to Main Menu 🔙")
        
        choice = input("Choose an option: ")

        if choice == "1":
            vacation_facade.add_vacation()
        elif choice == "2":
            vacation_facade.update_vacation()
        elif choice == "3":
            vacation_facade.delete_vacation()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice. Please try again!")


def main_menu(user_role, user_id):
    while True:
        print("\n=== Main Menu ===")
        if user_role == "admin":
            print("1. Manage Users 👥")
            print("2. Manage Countries 🌍")
            print("3. Manage Vacations 🏖️")
            print("4. Manage Likes ❤️")
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
                likes_facade.manage_likes(user_id=user_id)
            elif choice == "5":
                manage_roles()
            elif choice == "0":
                break
            else:
                print("\nInvalid choice. Please try again!")
        else:
            if choice == "1":
                vacation_facade.display_all_vacations()
            elif choice == "2":
                likes_facade.manage_likes(user_id=user_id)  # Pass user_id to likes management
            elif choice == "3":
                manage_countries()
            elif choice == "0":
                break
            else:
                print("\nInvalid choice. Please try again!")


def main():
    show_welcome_screen()
    user, user_role = login_or_signup()
    if user and user_role:  # Proceed only if user and user_role are valid
        main_menu(user_role, user['id'])  # Pass user_id to main_menu


if __name__ == "__main__":
    main()
