# main.py
import time
from facade.user_facade import UserFacade
from facade.vacations_facade import VacationFacade
from facade.likes_facade import LikesFacade
from facade.countries_facade import CountryFacade

vacation_facade = VacationFacade()
likes_facade = LikesFacade()
countries_facade = CountryFacade()

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
                return user, role  
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
        role = user['role_id'] 
        if role == 1:
            return user, "admin"
        elif role == 2:
            return user, "user"
        else:
            return user, "user"
    else:
        print("Invalid login credentials.")
        return None, None

def manage_countries():
    while True:
        print("\n=== Manage Countries ===")
        print("1. View Countries 🌍")
        print("2. Add Country ➕")
        print("0. Back to Main Menu 🔙")

        choice = input("Choose an option: ")

        if choice == "1":
            countries_facade.display_all_countries()
        elif choice == "2":
            countries_facade.add_country()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice. Please try again!")


def manage_vacations():
    while True:
        print("\n=== Manage Vacations ===")
        print("1. Add New Vacation 🏖️")
        print("2. Update Vacation Details 📝")
        print("3. Delete Vacation 🗑️")
        print("4. View Vacations 🏖️")

        print("0. Back to Main Menu 🔙")
        
        choice = input("Choose an option: ")

        if choice == "1":
            vacation_facade.add_vacation()
        elif choice == "2":
            vacation_facade.update_vacation()
        elif choice == "3":
            vacation_facade.delete_vacation()
        elif choice == "4":
            vacation_facade.display_all_vacations()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice. Please try again!")

def manage_users():
    while True:
        print("\n=== Manage Users ===")
        print("1. Show All Users 👥")
        print("2. Delete User 🗑️")
        print("0. Back to Main Menu 🔙")

        choice = input("Choose an option: ")

        if choice == "1":
            user_facade = UserFacade()  
            user_facade.display_all_users()
        elif choice == "2":
            user_facade = UserFacade() 
            user_facade.delete_user()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice. Please try again!")


def main_menu(user, role):
    while True:
        print("\n=== Main Menu ===")
        if role == "admin":
            print("1. Manage Users 👥")
            print("2. Manage Countries 🌍")
            print("3. Manage Vacations 🏖️")
        else:
            print("1. View Vacations 🏖️")
            print("2. Like Vacations ❤️")
            print("3. View Countries 🌍")

        print("0. Log Out 🔒")

        choice = input("Choose an option: ")

        if role == "admin":
            if choice == "1":
                manage_users()
            elif choice == "2":
                manage_countries()
            elif choice == "3":
                manage_vacations()
            elif choice == "0":
                print("\nLogging out...")
                time.sleep(2)
                return 
            else:
                print("Invalid choice. Please try again!")
        else:
            if choice == "1":
                vacation_facade.display_all_vacations()
            elif choice == "2":
                likes_facade.manage_likes(user_id=user['id'])
            elif choice == "3":
                countries_facade.display_all_countries()
            elif choice == "0":
                print("\nLogging out...")
                time.sleep(2)
                return  
            else:
                print("Invalid choice. Please try again!")




def main():
    show_welcome_screen()
    while True:
        user, user_role = login_or_signup()
        if user and user_role:  
            main_menu(user_role, user['id']) 
    


if __name__ == "__main__":
    main()
