import sys
import os

# הוספת התיקייה הראשית של הפרויקט לנתיב החיפוש
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))


from facade.user_facade import UserFacade
from facade.countries_facade import CountryFacade
from facade.vacations_facade import VacationFacade
from facade.likes_facade import LikesFacade
from facade.roles_facade import RolesFacade


def main():
    while True:
        print("\n=== Vacation Management System ===")
        print("1. Manage Users")
        print("2. Manage Countries")
        print("3. Manage Vacations")
        print("4. Manage Likes")
        print("5. Manage Roles")
        print("0. Exit")

        choice = input("Choose an option: ")

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
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_users():
    user_facade = UserFacade()
    while True:
        print("\n--- Manage Users ---")
        print("1. View All Users")
        print("2. Register New User")
        print("3. Delete User")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            user_facade.display_all_users()
        elif choice == "2":
            user_facade.register_user()
        elif choice == "3":
            user_facade.delete_user()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_countries():
    country_facade = CountryFacade()
    while True:
        print("\n--- Manage Countries ---")
        print("1. View All Countries")
        print("2. Add New Country")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            country_facade.display_all_countries()
        elif choice == "2":
            country_facade.add_country()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_vacations():
    vacation_facade = VacationFacade()
    while True:
        print("\n--- Manage Vacations ---")
        print("1. View All Vacations")
        print("2. Add New Vacation")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            vacation_facade.display_all_vacations()
        elif choice == "2":
            vacation_facade.add_vacation()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_likes():
    likes_facade = LikesFacade()
    while True:
        print("\n--- Manage Likes ---")
        print("1. View All Likes")
        print("2. Add Like")
        print("3. Remove Like")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            likes_facade.display_all_likes()
        elif choice == "2":
            likes_facade.add_like()
        elif choice == "3":
            likes_facade.remove_like()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_roles():
    roles_facade = RolesFacade()
    while True:
        print("\n--- Manage Roles ---")
        print("1. View All Roles")
        print("2. Add New Role")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            roles_facade.display_all_roles()
        elif choice == "2":
            roles_facade.add_role()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
